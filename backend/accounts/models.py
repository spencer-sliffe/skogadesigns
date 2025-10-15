from __future__ import annotations

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class Roles(models.TextChoices):
    CUSTOMER = "customer", _("Customer")
    STAFF    = "staff", _("Staff")           # NEW tier
    OWNER    = "owner", _("Owner")
    SUPERADMIN = "superadmin", _("Super Admin")



class User(AbstractUser):
    """
    Custom user model.
    - Use email as unique identifier for login.
    - Keep username field for admin compatibility but not required by us.
    """
    email = models.EmailField(_("email address"), unique=True)

    # OPTIONAL profile fields
    display_name = models.CharField(max_length=150, blank=True, default="")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]  # so createsuperuser still asks username

    def __str__(self) -> str:
        return self.email


class Tenant(models.Model):
    """
    A logical business container. For a single jewelry store today, you'll have one Tenant.
    This supports future multi-store (multi-tenant) out of the box.
    """
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)  # e.g., "skoga"
    # Optional: map domain if you ever go multi-domain per tenant
    domain = models.CharField(max_length=255, blank=True, default="")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class Membership(models.Model):
    """
    Many-to-many through model connecting Users to Tenants with a role.
    A single user can be owner on one tenant and customer on another.
    """
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE, related_name="memberships")
    tenant = models.ForeignKey("accounts.Tenant", on_delete=models.CASCADE, related_name="memberships")
    role = models.CharField(max_length=20, choices=Roles.choices, default=Roles.CUSTOMER)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = [("user", "tenant")]
        indexes = [
            models.Index(fields=["tenant", "role"]),
            models.Index(fields=["user", "role"]),
        ]

    def __str__(self) -> str:
        return f"{self.user.email} @ {self.tenant.slug} ({self.role})"
