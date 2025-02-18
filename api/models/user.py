from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    User model that extends the AbstractUser model.
    Methods:
        save(*args, **kwargs): Overrides the save method to hash the password if it is not already hashed.
        __str__(): Returns a string representation of the user in the format '<username> first_name last_name'.
    """
    first_name = None
    last_name = None
    name = models.CharField(max_length=150)

    def save(self, *args, **kwargs):
        if not self.password.startswith('pbkdf2_sha256$'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
