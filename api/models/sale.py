from django.db import models

from api.models.character import Character
from api.models.item import Item


class Sale(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    seller = models.ForeignKey(
        Character, on_delete=models.CASCADE, related_name="sales")
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    price = models.FloatField()
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.seller.name} selling {self.item.name} for {self.price} euros"
