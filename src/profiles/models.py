from django.contrib.auth.models import AbstractUser
from django.db import models


class UserNet(AbstractUser):
    """ custom user model
    """
    GENDER = (
        ('male', 'male'),
        ('female', 'female')
    )
    middle_name = models.CharField(max_length=50)
    first_login = models.DateTimeField(null=True)
    phone = models.CharField(max_length=14)
    avatar = models.ImageField(upload_to='user/avatar/', blank=True, null=True)
    bio = models.TextField(null=True)
    github = models.CharField(max_length=500, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    gender = models.CharField(choices=GENDER, max_length=6, default='male')
    technology = models.ManyToManyField('Technology', related_name='users', blank=True)

    def followers_count(self):
        return self.users.count()

    def subscriptions_count(self):
        return self.followers.count()

    def groups_count(self):
        return self.groupsSub.count()


class Technology(models.Model):
    """ Technology model
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
