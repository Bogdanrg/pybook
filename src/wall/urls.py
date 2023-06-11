from django.urls import path, include
from .views import *


urlpatterns = [
    path('comment/<int:pk>', CommentsView.as_view({
        'post': 'create', 'put': 'update', 'delete': 'destroy'
    })),
    path('<int:pk>/', PostListView.as_view()),
    path('post/<int:pk>', PostView.as_view({
        'get': 'retrieve', 'post': 'create', 'put': 'update', 'delete': 'destroy'
    })),
]
