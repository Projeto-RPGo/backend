from django.db import models

from .npc import NPC


class Affiliation(models.Model):
    affiliation_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    leader = models.ForeignKey(
        NPC, on_delete=models.CASCADE, related_name="leader")
    subleader = models.ForeignKey(
        NPC, on_delete=models.CASCADE, related_name="subleader")

    def __str__(self):
        return self.name
