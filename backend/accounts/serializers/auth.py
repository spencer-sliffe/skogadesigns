from __future__ import annotations
from django.contrib.auth import get_user_model, password_validation
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from accounts.models import Membership, Roles

User = get_user_model()

class UserMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "first_name", "last_name", "display_name", "is_active"]

class SignupSerializer(serializers.Serializer):
    """
    Public MEMBER sign-up (Customer role only).
    """
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, trim_whitespace=False)
    first_name = serializers.CharField(required=False, allow_blank=True, default="")
    last_name  = serializers.CharField(required=False, allow_blank=True, default="")
    display_name = serializers.CharField(required=False, allow_blank=True, default="")

    def validate_email(self, value):
        if User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError(_("An account with this email already exists."))
        return value

    def validate_password(self, value):
        password_validation.validate_password(value)
        return value

    def create(self, validated_data):
        tenant = self.context.get("tenant")
        if tenant is None:
            raise serializers.ValidationError(_("Tenant is not configured for this request."))

        email = validated_data["email"].lower()
        username = email.split("@")[0]
        user = User.objects.create_user(
            email=email,
            username=username,  # keep for Django admin compatibility
            password=validated_data["password"],
            first_name=validated_data.get("first_name", ""),
            last_name=validated_data.get("last_name", ""),
            display_name=validated_data.get("display_name", ""),
            is_active=True,
        )
        Membership.objects.create(user=user, tenant=tenant, role=Roles.CUSTOMER)
        return user
