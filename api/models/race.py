from django.db import models


class Race(models.Model):
    """
    A class used to represent a Race.
    Attributes:
        name (str): The name of the race.
        description (str): The description of the race.
    """

    race_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name
