from django.shortcuts import render
from src.base.classes import List
from .models import Group
from .serializers import GroupListSerializer


class GroupList(List):
    queryset = Group.objects.all()
    serializer_class = GroupListSerializer
    