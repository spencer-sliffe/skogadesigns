# backend/api/urls.py
from django.urls import path, include
from .router import urlpatterns as api_router_urlpatterns

urlpatterns = [
    *api_router_urlpatterns,
]
