from django.contrib import admin
from .models import Follower


@admin.register(Follower)
class FollowerAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "subscriber")
    list_display_links = ("user", "subscriber")
