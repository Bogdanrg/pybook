from src.profiles.models import UserNet
from .models import Follower
from src.base.services import BaseCRUD


class FollowerCRUD(BaseCRUD):
    """ CRUD operations to followers
    """
    CRUD_MODEL = Follower

    @staticmethod
    def self_subscription(user, subscriber) -> bool:
        if user.id == subscriber.id:
            return True
        return False

    def subscribe(self, user, subscriber) -> None:
        self.CRUD_MODEL.objects.create(user=user, subscriber=subscriber)

    def remove_subscription(self, user, subscriber) -> None:
        obj = self.safe_get(user=user, subscriber=subscriber)
        obj.delete()


class UserNetCRUD(BaseCRUD):
    """ CRUD operations to followers
    """
    CRUD_MODEL = UserNet


follower_service = FollowerCRUD()
user_service = UserNetCRUD()
