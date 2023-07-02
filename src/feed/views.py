from rest_framework import permissions
from rest_framework.response import Response

from src.wall.serializers import ListPostSerializer, PostSerializer
from src.base.classes import MixedPermissionGenericViewSet
from .services import feed_service


class FeedView(MixedPermissionGenericViewSet):
    serializer_class = ListPostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = feed_service.get_post_list(request.user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = feed_service.get_single_post(kwargs.get('pk'))
        serializer = PostSerializer(instance)
        return Response(serializer.data)
