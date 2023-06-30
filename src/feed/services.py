from src.wall.models import Post
from src.followers.models import Follower


def feed(user):
    posts = Post.objects.filter(user__users__subscriber_id=1).order_by('-created_date') \
        .select_ralated('user').prefetch_related('comments')
