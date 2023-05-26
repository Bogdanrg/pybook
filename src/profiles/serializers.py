from rest_framework import serializers

from .models import UserNet


class UserNetSerializer(serializers.ModelSerializer):
    """
    Serializer for UserNet
    """
    avatar = serializers.ImageField(read_only=True)

    class Meta:
        model = UserNet
        exclude = ("password", "last_login", "is_active", "is_staff", "is_superuser", "groups", "user_permissions")


class UserNetPublicSerializer(serializers.ModelSerializer):
    """
    Serializer for Public userв
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
