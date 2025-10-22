from __future__ import annotations
from rest_framework import serializers
from common.serializers.field_acl import FieldACLSerializerMixin
from .base import _ctx_tenant, _ensure_same_tenant
from ..models import Variant, Product

class VariantSerializer(FieldACLSerializerMixin, serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.name", read_only=True)

    class Meta:
        model = Variant
        fields = [
            "id", "product", "product_name", "sku", "barcode",
            "price_cents_override", "cost_cents_override",
            "stock_quantity", "is_active", "created_at", "updated_at",
        ]

    def validate_product(self, prod: Product):
        tenant = _ctx_tenant(self)
        _ensure_same_tenant(prod.tenant, tenant, "Product belongs to a different tenant.")
        return prod
