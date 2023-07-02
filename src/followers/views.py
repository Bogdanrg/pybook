from rest_framework import generics, permissions, views, response
from .serializers import ListFollowerSerializer
from .models import Follower
from .services import follower_service, user_service


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
        user = user_service.safe_get(pk=pk)
        subscriber = user_service.safe_get(pk=request.user.id)
        if not user:
            return response.Response(status=404)
        if follower_service.self_subscription(user, subscriber):
            return response.Response(status=404)
        follower_service.subscribe(user, subscriber)
        return response.Response(status=201)

    def delete(self, request, pk):
        sub = follower_service.safe_get(user_id=pk, subscriber=request.user)
        if not sub:
            return response.Response(status=404)
        user = user_service.safe_get(pk=pk)
        subscriber = user_service.safe_get(pk=request.user.id)
        follower_service.remove_subscription(user, subscriber)
        return response.Response(status=204)
