from rest_framework import response

from src.base.classes import List
from .models import Group
from .serializers import GroupListSerializer, GroupSerializer, PrivateGroupSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from src.base.permissions import IsStaff
from src.base.classes import MixedPermissionGenericViewSet


class GroupList(List):
    queryset = Group.objects.all()
    serializer_class = GroupListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class GroupDetail(MixedPermissionGenericViewSet):
    """ Viewset for retrieving group
    """

    permission_classes = [IsAuthenticatedOrReadOnly]
    permission_classes_by_action = {
        'get': [IsStaff],
        'put': [IsStaff],
        'delete': [IsStaff]
    }

    def retrieve(self, request, *args, **kwargs):
        queryset = Group.objects.prefetch_related('group_posts').get(pk=self.kwargs.get('pk'))
        if queryset.is_private:
            serializer = PrivateGroupSerializer(queryset)
            return response.Response(serializer.data)
        else:
            serializer = GroupSerializer(queryset)
            return response.Response(serializer.data)
