from django.db import models
from performer.models import Performer


class Album(models.Model):
    title = models.CharField(max_length=120)
    performer = models.ForeignKey(Performer, on_delete=models.CASCADE)
    year = models.IntegerField()

    def __str__(self):
        return f'{self.title}'
