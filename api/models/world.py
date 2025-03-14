from django.db import models

from .user import User


class World(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="created_worlds")
    created_at = models.DateTimeField(auto_now=True, editable=False)
    admins = models.ManyToManyField(User, related_name="admin_worlds")
    users = models.ManyToManyField(User, related_name="worlds")
