from django.urls import path
from . import views

urlpatterns = [
    path('', views.GroupList.as_view()),
    path('<int:pk>', views.GroupDetail.as_view({'get': 'retrieve',
                                                }))
]
