# api/router.py
from rest_framework_nested import routers
from accounts.views.auth import AuthViewSet  # import explicitly

router = routers.DefaultRouter(trailing_slash=False)
router.register("auth", AuthViewSet, basename="auth")

urlpatterns = [*router.urls]