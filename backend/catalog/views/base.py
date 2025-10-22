from __future__ import annotations
from rest_framework.permissions import BasePermission, SAFE_METHODS
from common.viewsets import TenantScopedModelViewSet  # your shared mixin/base
from accounts.models import Roles
from accounts.roles import has_role_at_least

class WriteGuard(BasePermission):
    """
    Public read (SAFE methods). Writes require STAFF (or above) for current tenant.
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return has_role_at_least(request.user, getattr(request, "tenant", None), Roles.STAFF)
