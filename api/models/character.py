from django.db import models

from .affiliation import Affiliation
from .skill import Skill
from .mcf import MCF
from .specialization import Specialization
from .maxdom import MaxDom
from .domain import Domain
from .race import Race
from .user import User

class Character(models.Model):
    """
    A class used to represent a character.
    Attributes:
        player_id (int): The id of the player who owns the character.
        character_id (int): The character's id.
        name (str): The name of the character.
        age (int): The age of the character.
        appearance (str): The appearance of the character.
        race (int): The id of the race of the character.
        affiliation (int): The id of the affiliation of the character.
        xp (int): The ammount of xp of the character.
        euros (float): The ammount of money of the character.
        personality (str): The personality of the character.
        background (str): The background of the character.
        status (str): The status of the character.
        rank (str): The rank of the character.
        idDom1 (int): The first domain of the character.
        idDom2 (int): The second domain of the character.
    """
    character_id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    avatar = models.TextField(null=True, blank=True)
    appearance = models.CharField(max_length=100)
    race = models.ForeignKey(Race, on_delete=models.DO_NOTHING, null=False)
    affiliation = models.ForeignKey(Affiliation, on_delete=models.DO_NOTHING, blank=True, default=None)
    xp = models.IntegerField(default=0)
    euros = models.FloatField(default=0)
    personality = models.TextField()
    background = models.TextField()
    status = models.CharField(max_length=50)
    rank = models.CharField(max_length=50)
    domain1_id = models.ForeignKey(Domain, blank=True, on_delete=models.DO_NOTHING, related_name="domain_1", default=None)
    domain2_id = models.ForeignKey(Domain, blank=True, on_delete=models.DO_NOTHING, related_name="domain_2", default=None)
    skills = models.ManyToManyField(Skill, through="SkillMastery", blank=True)
    mcfs = models.ManyToManyField(MCF, through="MCFMastery",blank=True)
    specializations = models.ManyToManyField(Specialization, through="SpecializationMastery", blank=True)
    maxdoms = models.ManyToManyField(MaxDom, through="MaxDomMastery", blank=True)

    def __str__(self):
        return self.name + ", XP: " + self.xp
    
class SkillMastery(models.Model):
    player_id = models.ForeignKey(Character, on_delete=models.CASCADE, related_name="skills")
    skill_id = models.ForeignKey(Skill, on_delete=models.CASCADE)
    slot = models.IntegerField()

class MCFMastery(models.Model):
    player_id = models.ForeignKey(Character, on_delete=models.CASCADE, related_name="mcfs")
    mcf_id = models.ForeignKey(MCF, on_delete=models.CASCADE)
    slot = models.IntegerField()

class SpecializationMastery(models.Model):
    player_id = models.ForeignKey(Character, on_delete=models.CASCADE, related_name="specializations")
    specialization_id = models.ForeignKey(Specialization, on_delete=models.CASCADE)

class MaxDomMastery(models.Model):
    player_id = models.ForeignKey(Character, on_delete=models.CASCADE, related_name="maxdoms")
    mcf_id = models.ForeignKey(MaxDom, on_delete=models.CASCADE)
