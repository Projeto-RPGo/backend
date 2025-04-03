from django.db import models

from .domain import Domain


class Skill(models.Model):
    skill_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    domain1 = models.ForeignKey(
        Domain, blank=False, on_delete=models.DO_NOTHING, related_name="skill_domain1")
    domain2 = models.ForeignKey(
        Domain, blank=True, on_delete=models.DO_NOTHING, related_name="skill_domain2")
    slot1 = models.TextField(blank=True)
    slot2 = models.TextField(blank=True)
    slot3 = models.TextField(blank=True)
    slot4 = models.TextField(blank=True)
    slot5 = models.TextField(blank=True)

    def __str__(self):
        return "Habilidade: " + self.name
