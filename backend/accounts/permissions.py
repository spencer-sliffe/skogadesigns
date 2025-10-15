from rest_framework.permissions import BasePermission, SAFE_METHODS
from accounts.models import Roles, Membership

class IsSuperAdmin(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user or not user.is_authenticated:
            return False
        if user.is_superuser:
            return True
        return Membership.objects.filter(user=user, role=Roles.SUPERADMIN).exists()

class IsTenantOwner(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user or not user.is_authenticated or not request.tenant:
            return False
        if user.is_superuser:
            return True
        return Membership.objects.filter(user=user, tenant=request.tenant, role=Roles.OWNER).exists()

class IsTenantStaffOrAbove(BasePermission):
    """
    Grants access if user is STAFF, OWNER, or SUPERADMIN for this tenant.
    """
    def has_permission(self, request, view):
        user = request.user
        if not user or not user.is_authenticated or not request.tenant:
            return False
        if user.is_superuser:
            return True
        return Membership.objects.filter(
            user=user,
            tenant=request.tenant,
            role__in=[Roles.STAFF, Roles.OWNER, Roles.SUPERADMIN],
        ).exists()

class IsCustomerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        user = request.user
        if not user or not user.is_authenticated or not request.tenant:
            return False
        return Membership.objects.filter(
            user=user,
            tenant=request.tenant,
            role__in=[Roles.CUSTOMER, Roles.STAFF, Roles.OWNER, Roles.SUPERADMIN],
        ).exists()
