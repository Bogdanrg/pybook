from .serializers import UserNetSerializer
from .models import UserNet
from rest_framework.generics import RetrieveAPIView


class GetUserNetAPIView(RetrieveAPIView):
    queryset = UserNet.objects.all()
    serializer_class = UserNetSerializer
