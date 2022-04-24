"""Create custom user model inheritate from native Django's user model."""
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """
    Users within the Django authentication system
    are represented by this model.
    Username and password are required. Other fields are optional.
    """

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'