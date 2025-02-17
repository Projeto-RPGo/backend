from django.db import models

from .user import User


class World(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    users = models.ManyToManyField(User, related_name='worlds')

    def __str__(self):
        return self.name
