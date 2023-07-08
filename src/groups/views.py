from src.base.classes import List, RetrieveUpdateDestroy
from .models import Group
from .serializers import GroupListSerializer, GroupSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from src.base.permissions import IsAuthor


class GroupList(List):
    queryset = Group.objects.all()
    serializer_class = GroupListSerializer
    permission_classes = [AllowAny]


class PublicGroupDetail(RetrieveUpdateDestroy):
    """ Viewset for retrieving group
    """
    queryset = Group.objects.filter(is_private=False).prefetch_related('group_posts')
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    permission_classes_by_action = {
        'get': [AllowAny],
        'put': [IsAuthor],
        'delete': [IsAuthor]
    }
