from django.urls import path
from .views import *


urlpatterns = [
    path('<int:user_pk>', GetUserNetAPIView.as_view()),
]
