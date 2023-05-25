from rest_framework import serializers

from .models import UserNet


class UserNetSerializer(serializers.ModelSerializer):
    """
    Serializer for UserNet
    """
    class Meta:
        model = UserNet
        exclude = ("password", "last_login", "is_active", "is_staff", "is_superuser", "groups", "user_permissions")


class UserNetPublicSerializer(serializers.ModelSerializer):
    """
    Serializer for Public user
    """
    class Meta:
        model = UserNet
        exclude = (
            "email",
            "phone",
            "password",
            "last_login",
            "is_active",
            "is_staff",
            "is_superuser",
            "groups",
            "user_permissions"
        )
