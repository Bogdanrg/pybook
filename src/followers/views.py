from rest_framework import generics, permissions, views, response
from .serializers import ListFollowerSerializer
from .models import Follower
from src.profiles.models import UserNet


class ListFollowerView(generics.ListAPIView):
    """ user's Follower list
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ListFollowerSerializer

    def get_queryset(self):
        return Follower.objects.filter(user=self.request.user)


class AddFollowerView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        user = UserNet.objects.safe_get(pk=pk)
        if user:
            Follower.objects.create(subscriber=request.user, user=user)
        return response.Response(status=404)
