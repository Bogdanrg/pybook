from django.urls import path, include
from .views import *


urlpatterns = [
    path('comment/', CommentsView.as_view({'post': 'create'})),
    path('comment/<int:pk>', CommentsView.as_view({'put': 'update', 'delete': 'destroy'})),
    path('post/', PostView.as_view({'post': 'create'})),
    path('<int:pk>/', PostListView.as_view()),
    path('post/<int:pk>', PostView.as_view({
        'get': 'retrieve', 'put': 'update', 'delete': 'destroy'
    })),
]
