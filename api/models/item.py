from django.db import models

from api.models.character import Character


class Item(models.Model):
    name = models.CharField(max_length=100)
    image = models.TextField(null=True, blank=True)
    description = models.TextField()
    character_id = models.ForeignKey(
        Character, on_delete=models.CASCADE, null=True, blank=True)
