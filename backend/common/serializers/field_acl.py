# backend/common/serializers/field_acl.py
from typing import Any, Dict
from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied
from accounts.models import Roles
from accounts.roles import has_role_at_least

ReadRule = Any   # "public" | "auth" | Roles
WriteRule = Any  # "public" | "auth" | Roles

def _can_read(user, tenant, rule: ReadRule) -> bool:
    if rule == "public":
        return True
    if rule == "auth":
        return bool(user and getattr(user, "is_authenticated", False))
    if isinstance(rule, Roles.__class__) or rule in Roles.values:
        return has_role_at_least(user, tenant, rule)  # type: ignore
    # default deny if unknown
    return False

def _can_write(user, tenant, rule: WriteRule) -> bool:
    # writes never allowed for anonymous unless explicitly "public"
    if rule == "public":
        return True
    if rule == "auth":
        return bool(user and getattr(user, "is_authenticated", False))
    if isinstance(rule, Roles.__class__) or rule in Roles.values:
        return has_role_at_least(user, tenant, rule)  # type: ignore
    return False

class FieldACLSerializerMixin(serializers.Serializer):
    """
    Enforces per-field read/write ACL based on request.user and request.tenant.
    Declare FIELD_ACL = { "field": {"read": RULE, "write": RULE}, ... }
    """
    # Example default: readable by anyone, writable by STAFF+
    FIELD_ACL: Dict[str, Dict[str, Any]] = {}

    def _ctx(self):
        request = self.context.get("request")
        user = getattr(request, "user", None)
        tenant = getattr(request, "tenant", None)
        return user, tenant

    # Hide unreadable fields dynamically
    def get_fields(self):
        fields = super().get_fields()
        user, tenant = self._ctx()
        acl = getattr(self, "FIELD_ACL", {}) or {}
        # If no ACL for a field → default read=public, write=auth
        for name in list(fields.keys()):
            rules = acl.get(name, {"read": "public", "write": "auth"})
            if not _can_read(user, tenant, rules.get("read", "public")):
                fields.pop(name, None)
        return fields

    # Block writes to non-writable fields
    def validate(self, attrs):
        user, tenant = self._ctx()
        acl = getattr(self, "FIELD_ACL", {}) or {}
        read_only_errors = []

        # For updates, compare incoming attrs to instance; for create, any provided field is a write
        for name, value in attrs.items():
            rules = acl.get(name, {"read": "public", "write": "auth"})
            can_w = _can_write(user, tenant, rules.get("write", "auth"))
            if not can_w:
                read_only_errors.append(name)

        if read_only_errors:
            raise PermissionDenied(f"You are not allowed to write: {', '.join(read_only_errors)}")

        return super().validate(attrs)
