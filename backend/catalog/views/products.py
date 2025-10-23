# backend/catalog/views/products.py
from __future__ import annotations
from .base import TenantScopedModelViewSet
from ..models import Product
from ..serializers import ProductSerializer
from ..permissions import CatalogWriteGuard

class ProductViewSet(TenantScopedModelViewSet):
    queryset = Product.objects.select_related("tenant", "category")
    serializer_class = ProductSerializer
    permission_classes = [CatalogWriteGuard]

    def get_queryset(self):
        tenant = getattr(self.request, "tenant", None)
        return super().get_queryset().filter(tenant=tenant)
