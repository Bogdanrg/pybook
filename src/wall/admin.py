from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from src.wall.models import Comment, Post




@admin.register(Comment)
class CommentAdmin(MPTTModelAdmin, admin.ModelAdmin):
    """ Comments on posts
    """
    list_display = ("user", "post", "created_date", "updated_at", "published", "id")
    mptt_level_indent = 15
