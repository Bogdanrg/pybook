from rest_framework import serializers

from .models import UserNet, Technology


class UserNetSerializer(serializers.ModelSerializer):
    """
    Serializer for UserNet
    """
    avatar = serializers.ImageField(read_only=True)
    followers_count = serializers.CharField(read_only=True)
    subscriptions_count = serializers.CharField(read_only=True)

    class Meta:
        model = UserNet
        exclude = ("password", "last_login", "is_active", "is_staff", "is_superuser", "groups", "user_permissions")


class UserNetPublicSerializer(serializers.ModelSerializer):
    """
    Serializer for Public users
    """
    followers_count = serializers.CharField(read_only=True)
    subscriptions_count = serializers.CharField(read_only=True)

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


class UserByFollowerSerializer(serializers.ModelSerializer):

    avatar = serializers.ImageField(read_only=True)

    class Meta:
        model = UserNet
        fields = ("id", "username", "avatar")
