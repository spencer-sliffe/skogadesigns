from __future__ import annotations
from rest_framework import serializers
from common.serializers.field_acl import FieldACLSerializerMixin
from .base import _ctx_tenant, _ensure_same_tenant
from ..models import Product, Category

class ProductSerializer(FieldACLSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id", "tenant", "category", "name", "slug", "description",
            "price_cents", "cost_cents", "sku", "is_active", "created_at", "updated_at",
        ]

    def validate_category(self, cat: Category | None):
        if not cat:
            return cat
        tenant = _ctx_tenant(self)
        _ensure_same_tenant(cat.tenant, tenant, "Category belongs to a different tenant.")
        return cat

    def create(self, validated_data):
        if not validated_data.get("tenant"):
            t = _ctx_tenant(self)
            if t:
                validated_data["tenant"] = t
        return super().create(validated_data)
