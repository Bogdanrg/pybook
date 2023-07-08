from rest_framework import serializers
from .models import Group, GroupPost
from src.profiles.serializers import TechnologyListSerializer


class GroupListSerializer(serializers.ModelSerializer):
    """ Serializer for group list
    """
    avatar = serializers.ImageField(read_only=True)
    technology = TechnologyListSerializer(many=True, read_only=True)
    members_count = serializers.CharField(read_only=True)

    class Meta:
        model = Group
        fields = ('name', 'avatar', 'technology', 'members_count')


class GroupPostListSerializer(serializers.ModelSerializer):
    """ Group post list serializer
    """

    class Meta:
        model = GroupPost
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    """ Detail Group serializer
    """
    group_posts = GroupPostListSerializer(many=True)
    members_count = serializers.CharField(read_only=True)
    avatar = serializers.CharField(read_only=True)
    technology = TechnologyListSerializer(many=True)

    class Meta:
        model = Group
        fields = ('name', 'group_posts', 'members_count', 'avatar', 'technology') # finish it


class PrivateGroupSerializer(serializers.ModelSerializer):
    """ Private detail Group serializer
    """
    members_count = serializers.CharField(read_only=True)
    avatar = serializers.CharField(read_only=True)
    technology = TechnologyListSerializer(many=True)

    class Meta:
        model = Group
        fields = ('name', 'avatar', 'members_count', 'technology')
