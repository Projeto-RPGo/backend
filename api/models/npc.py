from django.db import models

class NPC(models.Model):
    npc_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    title = models.CharField(max_length=50)
    association = models.CharField(max_length=50)

    def __str__(self):
        return self.name