from .serializers import UserNetSerializer
from .models import UserNet
from rest_framework.generics import RetrieveAPIView, UpdateAPIView
from rest_framework import permissions


class GetUserNetAPIView(RetrieveAPIView):
    """ Print user information """
    lookup_url_kwarg = 'user_pk'
    queryset = UserNet.objects.all()
    serializer_class = UserNetSerializer


class UpdateUserNetAPIView(UpdateAPIView):
    """
    Updates user information
    """
    lookup_url_kwarg = 'user_pk'
    serializer_class = UserNetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserNet.objects.filter(id=self.request.user.id)
