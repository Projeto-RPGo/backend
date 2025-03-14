from django.db import models

from .skill import Skill


class MCF(models.Model):
    mcf_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    skill_id = models.ForeignKey(Skill, on_delete=models.CASCADE, blank=False)
    slot1 = models.TextField()
    slot2 = models.TextField()
    slot3 = models.TextField()
    slot4 = models.TextField()
    slot5 = models.TextField()

    def __str__(self):
        return "MCF: " + self.name
