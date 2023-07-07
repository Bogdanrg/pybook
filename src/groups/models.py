from django.db import models
from src.profiles.models import Technology
from src.profiles.models import UserNet
from src.wall.models import Post


class GroupPost(Post):
    """ Post model for groups
    """
    group_id = models.ForeignKey('Group', on_delete=models.CASCADE)


class Group(models.Model):
    """ Group model
    """
    avatar = models.ImageField(upload_to='group/avatar')
    name = models.CharField(max_length=50)
    is_private = models.BooleanField(default=True)
    technology = models.ManyToManyField(Technology, related_name='groups')
    user = models.ManyToManyField(UserNet,
                                  through='GroupMembership',
                                  related_name='groupsSub')

    def __str__(self):
        return f"{self.name}"


class GroupMembership(models.Model):
    """ Through table for groups
    """
    group = models.ForeignKey('Group', on_delete=models.CASCADE)
    user = models.ForeignKey(UserNet, on_delete=models.CASCADE)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
