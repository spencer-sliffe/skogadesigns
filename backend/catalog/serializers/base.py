from __future__ import annotations
from rest_framework import serializers
from accounts.models import Tenant

def _ctx_req(serializer) -> "rest_framework.request.Request | None":
    return serializer.context.get("request")

def _ctx_tenant(serializer) -> Tenant | None:
    req = _ctx_req(serializer)
    return getattr(req, "tenant", None) if req else None

def _ensure_same_tenant(obj_tenant: Tenant | None, tenant: Tenant | None, msg: str):
    if not tenant or not obj_tenant or getattr(obj_tenant, "id", None) != getattr(tenant, "id", None):
        raise serializers.ValidationError(msg)
