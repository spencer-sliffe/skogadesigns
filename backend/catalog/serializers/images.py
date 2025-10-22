from __future__ import annotations
from rest_framework import serializers
from common.serializers.field_acl import FieldACLSerializerMixin
from .base import _ctx_tenant, _ensure_same_tenant
from ..models import ProductImage, Product

class ProductImageSerializer(FieldACLSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ["id", "product", "alt", "image_url", "sort_order", "created_at", "updated_at"]

    def validate_product(self, prod: Product):
        tenant = _ctx_tenant(self)
        _ensure_same_tenant(prod.tenant, tenant, "Product belongs to a different tenant.")
        return prod
