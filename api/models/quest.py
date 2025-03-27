from django.db import models
from .user import User
from .character import Character


class Quest(models.Model):
    quest_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    giver = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    participants = models.ManyToManyField(Character, related_name="quests", through="QuestMember")
    max_player_xp = models.IntegerField()
    min_level = models.IntegerField()
    max_level = models.IntegerField()
    max_giver_xp = models.IntegerField()
    type = models.TextField()
    narrations = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.type + ": " + self.quest_id

class QuestMember(models.Model):
    character_id = models.ForeignKey(Character, on_delete=models.DO_NOTHING)
    quest_id = models.ForeignKey(Quest, on_delete=models.CASCADE)
    xp = models.IntegerField()
    euros = models.IntegerField()