# backend/accounts/roles.py
from accounts.models import Roles, Membership

ROLE_RANK = {
    Roles.CUSTOMER: 1,
    Roles.STAFF: 2,
    Roles.OWNER: 3,
    Roles.SUPERADMIN: 4,
}

def has_role_at_least(user, tenant, min_role: Roles) -> bool:
    if not user or not getattr(user, "is_authenticated", False) or tenant is None:
        return False
    if user.is_superuser:
        return True
    role = (
        Membership.objects
        .filter(user=user, tenant=tenant)
        .values_list("role", flat=True)
        .first()
    )
    return ROLE_RANK.get(role, 0) >= ROLE_RANK[min_role]
