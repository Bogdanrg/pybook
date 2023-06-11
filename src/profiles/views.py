from .serializers import UserNetSerializer, UserNetPublicSerializer
from .models import UserNet
from rest_framework.generics import RetrieveAPIView, UpdateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions


class UserNetPublicViewSet(ModelViewSet):
    lookup_url_kwarg = 'user_pk'
    queryset = UserNet.objects.all()
    serializer_class = UserNetPublicSerializer
    permission_classes = [permissions.AllowAny]


class UserNetViewSet(ModelViewSet):
    lookup_url_kwarg = 'user_pk'
    serializer_class = UserNetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserNet.objects.filter(id=self.request.user.id)
