from src.wall.models import Post
from django.conf import settings


class Feed:
    """ Service feeds
    """
    @staticmethod
    def get_post_list(user: settings.AUTH_USER_MODEL):
        return Post.objects.filter(user__users__subscriber=user).order_by('-created_date') \
            .select_related('user').prefetch_related('comments')
    @staticmethod
    def get_single_post(pk: int):
        return Post.objects.select_related('user').prefetch_related('comments').get(id=pk)


feed_service = Feed()
