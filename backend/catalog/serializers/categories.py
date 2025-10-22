from __future__ import annotations
from rest_framework import serializers
from common.serializers.field_acl import FieldACLSerializerMixin
from accounts.models import Tenant
from .base import _ctx_tenant, _ensure_same_tenant
from ..models import Category

class CategorySerializer(FieldACLSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id", "tenant", "name", "slug", "description",
            "parent", "is_active", "created_at", "updated_at",
        ]

    def validate_parent(self, parent: Category | None):
        if parent is None:
            return parent
        tenant = _ctx_tenant(self)
        _ensure_same_tenant(parent.tenant, tenant, "Parent category belongs to a different tenant.")
        return parent

    def create(self, validated_data):
        if not validated_data.get("tenant"):
            t = _ctx_tenant(self)
            if t:
                validated_data["tenant"] = t
        return super().create(validated_data)
