from rest_framework import serializers
from .models import Group, GroupPost
from src.profiles.serializers import TechnologyListSerializer


class GroupListSerializer(serializers.ModelSerializer):
    """ Serializer for group list
    """
    avatar = serializers.ImageField(read_only=True)
    technology = TechnologyListSerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = ('name', 'avatar', 'technology')


class GroupPostListSerializer(serializers.ModelSerializer):
    """ Group post list serializer
    """

    class Meta:
        model = GroupPost
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    """ Detail Group serializer
    """
    post = GroupPostListSerializer(many=True)

    class Meta:
        model = Group
        fields = '__all__'


class PrivateGroupSerializer(serializers.ModelSerializer):
    """ Private detail Group serializer
    """

    class Meta:
        model = Group
        fields = '__all__'
