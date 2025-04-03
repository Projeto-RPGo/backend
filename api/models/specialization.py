from django.db import models

from .skill import Skill


class Specialization(models.Model):
    specialization_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    skill_id = models.ForeignKey(Skill, on_delete=models.CASCADE, blank=False)
    description = models.TextField()

    def __str__(self):
        return "Especialização: " + self.name
