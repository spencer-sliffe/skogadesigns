# backend/accounts/views/auth.py
from __future__ import annotations

from django.contrib.auth import get_user_model
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer,
    TokenRefreshSerializer,
    TokenVerifySerializer,
)
from rest_framework_simplejwt.tokens import RefreshToken

from drf_spectacular.utils import extend_schema, OpenApiResponse

from accounts.serializers import SignupSerializer, UserMeSerializer

User = get_user_model()


class AuthViewSet(viewsets.ViewSet):
    """
    Authentication endpoints for all user tiers.
    - POST /api/auth/signup
    - POST /api/auth/signin
    - POST /api/auth/refresh
    - POST /api/auth/verify
    - GET  /api/auth/me
    """

    @extend_schema(
        tags=["Auth"],
        operation_id="authSignup",
        request=SignupSerializer,
        responses={201: OpenApiResponse(response=UserMeSerializer, description="User created")},
    )
    @action(methods=["post"], detail=False, permission_classes=[AllowAny], url_path="signup")
    def signup(self, request):
        """Member signup only (Customers)."""
        serializer = SignupSerializer(
            data=request.data,
            context={"tenant": getattr(request, "tenant", None)},
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        refresh = RefreshToken.for_user(user)
        return Response(
            {
                "user": UserMeSerializer(user).data,
                "access": str(refresh.access_token),
                "refresh": str(refresh),
            },
            status=status.HTTP_201_CREATED,
        )

    @extend_schema(
        tags=["Auth"],
        operation_id="authSignin",
        request=TokenObtainPairSerializer,
        responses={200: OpenApiResponse(description="JWT tokens and user info")},
    )
    @action(methods=["post"], detail=False, permission_classes=[AllowAny], url_path="signin")
    def signin(self, request):
        """Sign in for all roles (Customer, Staff, Owner, SuperAdmin)."""
        serializer = TokenObtainPairSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        email = (request.data.get("email") or "").lower()
        try:
            user = User.objects.get(email=email)
            data["user"] = UserMeSerializer(user).data
        except User.DoesNotExist:
            data["user"] = None

        return Response(data, status=200)

    @extend_schema(tags=["Auth"], operation_id="authRefresh", request=TokenRefreshSerializer)
    @action(methods=["post"], detail=False, permission_classes=[AllowAny], url_path="refresh")
    def refresh(self, request):
        """Refresh JWT token."""
        s = TokenRefreshSerializer(data=request.data)
        s.is_valid(raise_exception=True)
        return Response(s.validated_data, status=200)

    @extend_schema(tags=["Auth"], operation_id="authVerify", request=TokenVerifySerializer)
    @action(methods=["post"], detail=False, permission_classes=[AllowAny], url_path="verify")
    def verify(self, request):
        """Verify JWT token."""
        s = TokenVerifySerializer(data=request.data)
        s.is_valid(raise_exception=True)
        return Response({}, status=200)

    @extend_schema(tags=["Auth"], operation_id="authMe", responses={200: UserMeSerializer})
    @action(methods=["get"], detail=False, permission_classes=[IsAuthenticated], url_path="me")
    def me(self, request):
        """Get the authenticated user's profile."""
        return Response(UserMeSerializer(request.user).data, status=200)
