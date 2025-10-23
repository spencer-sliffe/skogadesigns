# backend/catalog/views/categories.py
from __future__ import annotations
from .base import TenantScopedModelViewSet
from ..models import Category
from ..serializers import CategorySerializer
from ..permissions import CatalogWriteGuard

class CategoryViewSet(TenantScopedModelViewSet):
    queryset = Category.objects.select_related("tenant", "parent")
    serializer_class = CategorySerializer
    permission_classes = [CatalogWriteGuard]

    def get_queryset(self):
        tenant = getattr(self.request, "tenant", None)
        return super().get_queryset().filter(tenant=tenant)
