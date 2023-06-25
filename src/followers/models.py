from django.db import models
from django.conf import settings


class Follower(models.Model):
    """ Follower model
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='users')
    subscriber = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='followers')
