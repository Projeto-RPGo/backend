from django.db import models
from .user import User
from .race import Race
from .domain import Domain
from .affiliation import Affiliation

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
    player_id = models.ForeignKey(User, on_delete=models.CASCADE)
    character_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    appearance = models.URLField()
    race = models.ForeignKey(Race, on_delete=models.DO_NOTHING, null=False)
    affiliation = models.ForeignKey(Affiliation, on_delete=models.DO_NOTHING, blank=True, default=None)
    xp = models.IntegerField(default=0)
    euros = models.FloatField(default=0)
    personality = models.TextField()
    background = models.TextField()
    status = models.CharField(max_length=50)
    rank = models.CharField(max_length=50)
    idDom1 = models.ForeignKey(Domain, blank=True, on_delete=models.DO_NOTHING, related_name="domain_1", default=None)
    idDom2 = models.ForeignKey(Domain, blank=True, on_delete=models.DO_NOTHING, related_name="domain_2", default=None)

    def __str__(self):
        return self.name + ", XP: " + self.xp