from __future__ import annotations
from .base import WriteGuard
from common.viewsets import TenantScopedModelViewSet
from ..models import Attribute, AttributeValue, ProductAttribute
from ..serializers import AttributeSerializer, AttributeValueSerializer, ProductAttributeSerializer

class AttributeViewSet(TenantScopedModelViewSet):
    queryset = Attribute.objects.select_related("tenant")
    serializer_class = AttributeSerializer
    permission_classes = [WriteGuard]

    def get_queryset(self):
        tenant = getattr(self.request, "tenant", None)
        return super().get_queryset().filter(tenant=tenant)

class AttributeValueViewSet(TenantScopedModelViewSet):
    queryset = AttributeValue.objects.select_related("attribute", "attribute__tenant")
    serializer_class = AttributeValueSerializer
    permission_classes = [WriteGuard]
    tenant_path = "attribute__tenant"

    def get_queryset(self):
        tenant = getattr(self.request, "tenant", None)
        return super().get_queryset().filter(attribute__tenant=tenant)

class ProductAttributeViewSet(TenantScopedModelViewSet):
    queryset = ProductAttribute.objects.select_related("product", "product__tenant", "attribute", "value")
    serializer_class = ProductAttributeSerializer
    permission_classes = [WriteGuard]
    tenant_path = "product__tenant"

    def get_queryset(self):
        tenant = getattr(self.request, "tenant", None)
        return super().get_queryset().filter(product__tenant=tenant)
