from django.urls import path
from .views import *


urlpatterns = [
    path('add', AddFollowerView.as_view()),
    path('', ListFollowerView.as_view())
]
