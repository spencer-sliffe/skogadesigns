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
    Looks for rules in this order:
      1) Serializer.FIELD_ACL
      2) Model.FIELD_ACL (if serializer.Meta.model defines it)
      3) Default: read=public, write=auth
    """
    FIELD_ACL: Dict[str, Dict[str, Any]] = {}

    def _ctx(self):
        request = self.context.get("request")
        user = getattr(request, "user", None)
        tenant = getattr(request, "tenant", None)
        return user, tenant

    def _acl_map(self) -> Dict[str, Dict[str, Any]]:
        if getattr(self, "FIELD_ACL", None):
            return self.FIELD_ACL
        model = getattr(getattr(self, "Meta", None), "model", None)
        if model and hasattr(model, "FIELD_ACL"):
            return getattr(model, "FIELD_ACL")
        return {}

    def get_fields(self):
        fields = super().get_fields()
        user, tenant = self._ctx()
        acl = self._acl_map()
        for name in list(fields.keys()):
            rules = acl.get(name, {"read": "public", "write": "auth"})
            if not _can_read(user, tenant, rules.get("read", "public")):
                fields.pop(name, None)
        return fields

    def validate(self, attrs):
        user, tenant = self._ctx()
        acl = self._acl_map()
        blocked = []
        for name in attrs.keys():
            rules = acl.get(name, {"read": "public", "write": "auth"})
            if not _can_write(user, tenant, rules.get("write", "auth")):
                blocked.append(name)
        if blocked:
            raise PermissionDenied(f"You are not allowed to write: {', '.join(blocked)}")
        return super().validate(attrs)