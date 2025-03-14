from django.db import models


class Domain(models.Model):
    domain_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
