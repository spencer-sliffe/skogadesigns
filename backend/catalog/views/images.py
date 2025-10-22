from __future__ import annotations
from .base import WriteGuard
from common.viewsets import TenantScopedModelViewSet
from ..models import ProductImage
from ..serializers import ProductImageSerializer

class ProductImageViewSet(TenantScopedModelViewSet):
    queryset = ProductImage.objects.select_related("product", "product__tenant")
    serializer_class = ProductImageSerializer
    permission_classes = [WriteGuard]
    tenant_path = "product__tenant"  # indirect tenant scope

    def get_queryset(self):
        tenant = getattr(self.request, "tenant", None)
        return super().get_queryset().filter(product__tenant=tenant)
