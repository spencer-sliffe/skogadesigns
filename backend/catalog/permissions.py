# backend/catalog/permissions.py
from __future__ import annotations
from rest_framework.permissions import BasePermission, SAFE_METHODS
from accounts.models import Roles
from accounts.roles import has_role_at_least

class CatalogWriteGuard(BasePermission):
    """
    - SAFE methods (GET/HEAD/OPTIONS): public
    - CREATE/UPDATE/PATCH: STAFF or above
    - DELETE: OWNER or above
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        tenant = getattr(request, "tenant", None)
        if request.method == "DELETE":
            return has_role_at_least(request.user, tenant, Roles.OWNER)
        return has_role_at_least(request.user, tenant, Roles.STAFF)
