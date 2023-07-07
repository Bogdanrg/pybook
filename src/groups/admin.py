from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Group, GroupMembership


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_private', 'get_html_photo')
    list_display_links = ('id', 'name')
    readonly_fields = ('get_html_photo',)

    def get_html_photo(self, object):
        if object.avatar:
            return mark_safe(f'<img src="{object.avatar.url}" width=50px>')

    get_html_photo.short_description = 'avatar'


@admin.register(GroupMembership)
class GroupMembershipAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'group', 'date_joined', 'is_staff')
