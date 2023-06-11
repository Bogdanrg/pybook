from django.urls import path
from .views import *


urlpatterns = [
    path('profile/<int:user_pk>', UserNetViewSet.as_view({'get': 'retrieve', 'put': 'update'})),
    path('<int:user_pk>', UserNetPublicViewSet.as_view({'get': 'retrieve'}))
]
