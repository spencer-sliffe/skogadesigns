from __future__ import annotations

from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator
from accounts.models import Tenant, Roles


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(TimeStampedModel):
    """
    A hierarchical group (e.g., Rings, Necklaces).
    """
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name="categories")
    name = models.CharField(max_length=140)
    slug = models.SlugField(max_length=160)
    description = models.TextField(blank=True, default="")
    parent = models.ForeignKey(
        "self", null=True, blank=True, on_delete=models.CASCADE, related_name="children"
    )
    is_active = models.BooleanField(default=True)

    # ✅ Field-level ACL lives on the class (not in Meta)
    FIELD_ACL = {
        "id":          {"read": "public",      "write": Roles.SUPERADMIN},
        "tenant":      {"read": Roles.STAFF,   "write": Roles.OWNER},
        "name":        {"read": "public",      "write": Roles.STAFF},
        "slug":        {"read": "public",      "write": Roles.STAFF},
        "description": {"read": "public",      "write": Roles.STAFF},
        "parent":      {"read": "public",      "write": Roles.STAFF},
        "is_active":   {"read": "public",      "write": Roles.STAFF},
        "created_at":  {"read": "public",      "write": Roles.SUPERADMIN},
        "updated_at":  {"read": "public",      "write": Roles.SUPERADMIN},
    }

    class Meta:
        unique_together = [("tenant", "slug")]
        indexes = [
            models.Index(fields=["tenant", "slug"]),
            models.Index(fields=["tenant", "is_active"]),
            models.Index(fields=["tenant", "parent"]),
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)[:160]
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"[{self.tenant.slug}] {self.name}"


class Product(TimeStampedModel):
    """
    A sellable item (base product). Variants can override price/stock if needed.
    """
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name="products")
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL, related_name="products")

    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220)
    description = models.TextField(blank=True, default="")

    # Monetary values in cents to avoid floating precision.
    price_cents = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    cost_cents = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])

    sku = models.CharField(max_length=64, blank=True, default="", db_index=True)

    is_active = models.BooleanField(default=True)

    FIELD_ACL = {
        "id":           {"read": "public",      "write": Roles.SUPERADMIN},
        "tenant":       {"read": Roles.STAFF,   "write": Roles.OWNER},
        "category":     {"read": "public",      "write": Roles.STAFF},
        "name":         {"read": "public",      "write": Roles.STAFF},
        "slug":         {"read": "public",      "write": Roles.STAFF},
        "description":  {"read": "public",      "write": Roles.STAFF},
        "price_cents":  {"read": "public",      "write": Roles.OWNER},
        "cost_cents":   {"read": Roles.STAFF,   "write": Roles.OWNER},
        "sku":          {"read": "public",      "write": Roles.STAFF},
        "is_active":    {"read": "public",      "write": Roles.STAFF},
        "created_at":   {"read": "public",      "write": Roles.SUPERADMIN},
        "updated_at":   {"read": "public",      "write": Roles.SUPERADMIN},
    }

    class Meta:
        unique_together = [("tenant", "slug")]
        indexes = [
            models.Index(fields=["tenant", "slug"]),
            models.Index(fields=["tenant", "sku"]),
            models.Index(fields=["tenant", "is_active"]),
            models.Index(fields=["tenant", "category"]),
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)[:220]
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"[{self.tenant.slug}] {self.name}"


class ProductImage(TimeStampedModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    alt = models.CharField(max_length=180, blank=True, default="")
    image_url = models.URLField(max_length=800)  # or ImageField if using storage
    sort_order = models.PositiveIntegerField(default=0)

    FIELD_ACL = {
        "id":         {"read": "public",    "write": Roles.SUPERADMIN},
        "product":    {"read": "public",    "write": Roles.STAFF},
        "alt":        {"read": "public",    "write": Roles.STAFF},
        "image_url":  {"read": "public",    "write": Roles.STAFF},
        "sort_order": {"read": "public",    "write": Roles.STAFF},
        "created_at": {"read": "public",    "write": Roles.SUPERADMIN},
        "updated_at": {"read": "public",    "write": Roles.SUPERADMIN},
    }

    class Meta:
        indexes = [
            models.Index(fields=["product", "sort_order"]),
        ]

    def __str__(self) -> str:
        return f"Image for {self.product_id} ({self.sort_order})"


class Attribute(TimeStampedModel):
    """
    Generic attributes (Metal, Gemstone, Ring Size). Tenant-scoped.
    """
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name="attributes")
    name = models.CharField(max_length=140)
    slug = models.SlugField(max_length=160)

    FIELD_ACL = {
        "id":         {"read": "public",     "write": Roles.SUPERADMIN},
        "tenant":     {"read": Roles.STAFF,  "write": Roles.OWNER},
        "name":       {"read": "public",     "write": Roles.STAFF},
        "slug":       {"read": "public",     "write": Roles.STAFF},
        "created_at": {"read": "public",     "write": Roles.SUPERADMIN},
        "updated_at": {"read": "public",     "write": Roles.SUPERADMIN},
    }

    class Meta:
        unique_together = [("tenant", "slug")]
        indexes = [
            models.Index(fields=["tenant", "slug"]),
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)[:160]
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"[{self.tenant.slug}] {self.name}"


class AttributeValue(TimeStampedModel):
    """
    Possible values for an Attribute (e.g., for Metal: Gold, Silver; for Size: 6,7,8).
    """
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE, related_name="values")
    value = models.CharField(max_length=140)
    slug = models.SlugField(max_length=160)

    FIELD_ACL = {
        "id":         {"read": "public",     "write": Roles.SUPERADMIN},
        "attribute":  {"read": "public",     "write": Roles.STAFF},
        "value":      {"read": "public",     "write": Roles.STAFF},
        "slug":       {"read": "public",     "write": Roles.STAFF},
        "created_at": {"read": "public",     "write": Roles.SUPERADMIN},
        "updated_at": {"read": "public",     "write": Roles.SUPERADMIN},
    }

    class Meta:
        unique_together = [("attribute", "slug")]
        indexes = [
            models.Index(fields=["attribute", "slug"]),
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.value)[:160]
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.attribute.name}: {self.value}"


class ProductAttribute(TimeStampedModel):
    """
    Attach AttributeValue(s) to a Product (e.g., Metal=Gold, Size=7).
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="attributes")
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE, related_name="product_attributes")
    value = models.ForeignKey(AttributeValue, on_delete=models.CASCADE, related_name="product_attributes")

    FIELD_ACL = {
        "id":        {"read": "public",   "write": Roles.SUPERADMIN},
        "product":   {"read": "public",   "write": Roles.STAFF},
        "attribute": {"read": "public",   "write": Roles.STAFF},
        "value":     {"read": "public",   "write": Roles.STAFF},
        "created_at":{"read": "public",   "write": Roles.SUPERADMIN},
        "updated_at":{"read": "public",   "write": Roles.SUPERADMIN},
    }

    class Meta:
        unique_together = [("product", "attribute", "value")]
        indexes = [
            models.Index(fields=["product", "attribute"]),
        ]

    def __str__(self) -> str:
        return f"{self.product_id} • {self.attribute.slug}={self.value.slug}"


class Variant(TimeStampedModel):
    """
    SKU-level variant (e.g., Size 7 / White Gold).
    Overrides price/stock when set; otherwise falls back to product.price_cents.
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="variants")

    sku = models.CharField(max_length=64, db_index=True)
    barcode = models.CharField(max_length=64, blank=True, default="", db_index=True)

    price_cents_override = models.PositiveIntegerField(null=True, blank=True, validators=[MinValueValidator(0)])
    cost_cents_override = models.PositiveIntegerField(null=True, blank=True, validators=[MinValueValidator(0)])

    stock_quantity = models.IntegerField(default=0)  # allow negative to represent backorders
    is_active = models.BooleanField(default=True)

    FIELD_ACL = {
        "id":                   {"read": "public",    "write": Roles.SUPERADMIN},
        "product":              {"read": "public",    "write": Roles.STAFF},
        "sku":                  {"read": "public",    "write": Roles.STAFF},
        "barcode":              {"read": "public",    "write": Roles.STAFF},
        "price_cents_override": {"read": "public",    "write": Roles.OWNER},
        "cost_cents_override":  {"read": Roles.STAFF, "write": Roles.OWNER},
        "stock_quantity":       {"read": Roles.STAFF, "write": Roles.STAFF},
        "is_active":            {"read": "public",    "write": Roles.STAFF},
        "created_at":           {"read": "public",    "write": Roles.SUPERADMIN},
        "updated_at":           {"read": "public",    "write": Roles.SUPERADMIN},
    }

    class Meta:
        unique_together = [("product", "sku")]
        indexes = [
            models.Index(fields=["product", "sku"]),
            models.Index(fields=["product", "is_active"]),
        ]

    def __str__(self) -> str:
        return f"{self.product_id}:{self.sku}"
