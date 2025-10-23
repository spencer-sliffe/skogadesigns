# backend/catalog/views/images.py
from __future__ import annotations
from .base import TenantScopedModelViewSet
from ..models import ProductImage
from ..serializers import ProductImageSerializer
from ..permissions import CatalogWriteGuard

class ProductImageViewSet(TenantScopedModelViewSet):
    queryset = ProductImage.objects.select_related("product", "product__tenant")
    serializer_class = ProductImageSerializer
    permission_classes = [CatalogWriteGuard]
    tenant_path = "product__tenant"

    def get_queryset(self):
        tenant = getattr(self.request, "tenant", None)
        return super().get_queryset().filter(product__tenant=tenant)
