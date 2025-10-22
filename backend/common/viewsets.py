from typing import Optional
from rest_framework.viewsets import ModelViewSet

class TenantScopedQuerysetMixin:
    """
    Mixin that filters queryset by the current request.tenant.
    Set `tenant_path` to the field path that points to the Tenant FK.
      - Direct tenant FK: tenant_path = "tenant" (default)
      - Via relation:     tenant_path = "product__tenant", "category__tenant", etc.
    """
    tenant_path: str = "tenant"

    def get_tenant(self):
        # Your CurrentTenantMiddleware attaches request.tenant
        return getattr(self.request, "tenant", None)

    def get_queryset(self):
        base = super().get_queryset()
        tenant = self.get_tenant()
        if tenant is None:
            return base.none()
        return base.filter(**{self.tenant_path: tenant})


class TenantScopedModelViewSet(TenantScopedQuerysetMixin, ModelViewSet):
    """
    Convenience base class: ModelViewSet + tenant scoping.
    Override `tenant_path` per view if the FK is indirect.
    """
    pass
