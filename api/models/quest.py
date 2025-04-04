from django.db import models

from .character import Character
from .user import User


class Quest(models.Model):
    STATUS_CHOICES = [
        ("ACTIVE", "Active"),
        ("COMPLETED", "Completed"),
        ("CANCELED", "Canceled"),
    ]

    quest_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    giver = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    participants = models.ManyToManyField(
        Character, related_name="quests", through="QuestMember")
    max_player_xp = models.IntegerField()
    min_level = models.IntegerField()
    max_level = models.IntegerField()
    max_giver_xp = models.IntegerField()
    type = models.TextField()
    narrations = models.IntegerField()
    description = models.TextField()
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="ACTIVE"
    )

    def __str__(self):
        return self.type + ": " + str(self.quest_id)


class QuestMember(models.Model):
    character = models.ForeignKey(Character, on_delete=models.DO_NOTHING)
    quest = models.ForeignKey(Quest, on_delete=models.CASCADE)
    xp = models.IntegerField()
    euros = models.IntegerField()
