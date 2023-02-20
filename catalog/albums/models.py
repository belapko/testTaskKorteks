from django.db import models
from performer.models import Performer


class Album(models.Model):
    performer = models.ForeignKey(Performer, on_delete=models.CASCADE)
    year = models.IntegerField()
