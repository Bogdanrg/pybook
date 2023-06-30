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


class FollowerView(views.APIView):
    """ Subscribe to somebody and delete"""
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        try:
            user = UserNet.objects.get(pk=pk)
        except UserNet.DoesNotExist:
            return response.Response(status=404)
        Follower.objects.create(subscriber=request.user, user=user)
        return response.Response(status=201)

    def delete(self, request, pk):
        try:
            sub = Follower.objects.get(subscriber=request.user, user_id=pk)
        except Follower.DoesNotExist:
            return response.Response(status=404)
        sub.delete()
        response.Response(status=204)
