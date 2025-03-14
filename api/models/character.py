from django.db import models

from .affiliation import Affiliation
from .domain import Domain
from .maxdom import MaxDom
from .mcf import MCF
from .race import Race
from .skill import Skill
from .specialization import Specialization
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
    affiliation = models.ForeignKey(
        Affiliation, on_delete=models.DO_NOTHING, blank=True, default=None)
    xp = models.IntegerField(default=0)
    euros = models.FloatField(default=0)
    personality = models.TextField()
    background = models.TextField()
    status = models.CharField(max_length=50)
    rank = models.CharField(max_length=50)
    domain1 = models.ForeignKey(Domain, blank=True, on_delete=models.DO_NOTHING,
                                related_name="character_domain1", default=None)
    domain2 = models.ForeignKey(Domain, blank=True, on_delete=models.DO_NOTHING,
                                related_name="character_domain2", default=None)
    skills = models.ManyToManyField(
        Skill, related_name='character_skills', through="SkillMastery", blank=True)
    mcfs = models.ManyToManyField(
        MCF, related_name='character_mcfs', through="MCFMastery", blank=True)
    specializations = models.ManyToManyField(
        Specialization, related_name='character_specializations', through="SpecializationMastery", blank=True)
    maxdoms = models.ManyToManyField(
        MaxDom, related_name='character_maxdoms', through="MaxDomMastery", blank=True)

    def __str__(self):
        return self.name + ", XP: " + self.xp


class SkillMastery(models.Model):
    player_id = models.ForeignKey(
        Character, on_delete=models.CASCADE, related_name="skill_mastery")
    skill_id = models.ForeignKey(Skill, on_delete=models.CASCADE)
    slot = models.IntegerField()


class MCFMastery(models.Model):
    player_id = models.ForeignKey(
        Character, on_delete=models.CASCADE, related_name="mcf_mastery")
    mcf_id = models.ForeignKey(MCF, on_delete=models.CASCADE)
    slot = models.IntegerField()


class SpecializationMastery(models.Model):
    player_id = models.ForeignKey(
        Character, on_delete=models.CASCADE, related_name="specialization_mastery")
    specialization_id = models.ForeignKey(
        Specialization, on_delete=models.CASCADE)


class MaxDomMastery(models.Model):
    player_id = models.ForeignKey(
        Character, on_delete=models.CASCADE, related_name="maxdom_mastery")
    mcf_id = models.ForeignKey(MaxDom, on_delete=models.CASCADE)
