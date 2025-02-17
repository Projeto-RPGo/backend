from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    User model that extends the AbstractUser model.
    Methods:
        save(*args, **kwargs): Overrides the save method to hash the password if it is not already hashed.
        __str__(): Returns a string representation of the user in the format '<username> first_name last_name'.
    """

    def save(self, *args, **kwargs):
        if not self.password.startswith('pbkdf2_sha256$'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return '<' + self.username + '> ' + self.first_name + ' ' + self.last_name
