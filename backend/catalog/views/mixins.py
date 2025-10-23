# backend/catalog/views/mixins.py
from __future__ import annotations
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from accounts.models import Roles
from accounts.roles import has_role_at_least

class OwnerBulkDeleteMixin:
    """
    Adds POST /<resource>/bulk-delete  with payload {"ids":[...]}.
    Only OWNER+ of current tenant can use it.
    """
    @action(methods=["post"], detail=False, url_path="bulk-delete")
    def bulk_delete(self, request):
        tenant = getattr(request, "tenant", None)
        if not has_role_at_least(request.user, tenant, Roles.OWNER):
            return Response({"detail": "Owner role required."}, status=status.HTTP_403_FORBIDDEN)

        ids = request.data.get("ids") or []
        if not isinstance(ids, list) or not all(isinstance(i, int) for i in ids):
            return Response({"detail": "ids must be a list of integers."}, status=400)

        qs = self.get_queryset().filter(id__in=ids)
        deleted, _ = qs.delete()
        return Response({"deleted": deleted}, status=200)
