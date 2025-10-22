from __future__ import annotations
from rest_framework import serializers
from common.serializers.field_acl import FieldACLSerializerMixin
from .base import _ctx_tenant, _ensure_same_tenant
from ..models import Attribute, AttributeValue, ProductAttribute, Product

class AttributeSerializer(FieldACLSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = ["id", "tenant", "name", "slug", "created_at", "updated_at"]

    def create(self, validated_data):
        if not validated_data.get("tenant"):
            t = _ctx_tenant(self)
            if t:
                validated_data["tenant"] = t
        return super().create(validated_data)

class AttributeValueSerializer(FieldACLSerializerMixin, serializers.ModelSerializer):
    attribute_name = serializers.CharField(source="attribute.name", read_only=True)

    class Meta:
        model = AttributeValue
        fields = ["id", "attribute", "attribute_name", "value", "slug", "created_at", "updated_at"]

    def validate_attribute(self, attr: Attribute):
        tenant = _ctx_tenant(self)
        _ensure_same_tenant(attr.tenant, tenant, "Attribute belongs to a different tenant.")
        return attr

class ProductAttributeSerializer(FieldACLSerializerMixin, serializers.ModelSerializer):
    attribute_name = serializers.CharField(source="attribute.name", read_only=True)
    value_text = serializers.CharField(source="value.value", read_only=True)

    class Meta:
        model = ProductAttribute
        fields = ["id", "product", "attribute", "value", "attribute_name", "value_text", "created_at", "updated_at"]

    def validate(self, attrs):
        attrs = super().validate(attrs)
        prod: Product = attrs.get("product") or self.instance.product  # type: ignore
        attr: Attribute = attrs.get("attribute") or self.instance.attribute  # type: ignore
        val: AttributeValue = attrs.get("value") or self.instance.value  # type: ignore

        tenant = _ctx_tenant(self)
        _ensure_same_tenant(prod.tenant, tenant, "Product belongs to a different tenant.")
        _ensure_same_tenant(attr.tenant, tenant, "Attribute belongs to a different tenant.")
        if val.attribute_id != attr.id:
            raise serializers.ValidationError("AttributeValue does not belong to the given Attribute.")
        return attrs
