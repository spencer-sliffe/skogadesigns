from __future__ import annotations
from .base import WriteGuard
from common.viewsets import TenantScopedModelViewSet
from ..models import Variant
from ..serializers import VariantSerializer

class VariantViewSet(TenantScopedModelViewSet):
    queryset = Variant.objects.select_related("product", "product__tenant")
    serializer_class = VariantSerializer
    permission_classes = [WriteGuard]
    tenant_path = "product__tenant"

    def get_queryset(self):
        tenant = getattr(self.request, "tenant", None)
        return super().get_queryset().filter(product__tenant=tenant)
