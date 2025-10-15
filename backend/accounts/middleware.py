from django.utils.deprecation import MiddlewareMixin
from accounts.models import Tenant

class CurrentTenantMiddleware(MiddlewareMixin):
    """
    Resolve the current tenant once per request and attach it to request.tenant.
    Strategy:
      1) Match domain to Tenant.domain
      2) Fallback: first Tenant in DB
    """
    def process_request(self, request):
        host = (request.get_host() or "").split(":")[0].lower()
        tenant = None

        if host:
            try:
                tenant = Tenant.objects.get(domain=host)
            except Tenant.DoesNotExist:
                pass

        if not tenant:
            tenant = Tenant.objects.order_by("id").first()

        request.tenant = tenant
