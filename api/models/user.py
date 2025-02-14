from django.contrib.auth.hashers import make_password
from django.db import models


class User(models.Model):
    """
    A class used to represent a user.
    Attributes:
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
        username (str): The username of the user.
        email (str): The email of the user.
        password (str): The password of the user.
        date_joined (datetime): The date and time the user was created.
    """
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=128)
    date_joined = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.password.startswith('pbkdf2_sha256$'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' <' + self.username + '>'
