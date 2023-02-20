from django.db import models


class Performer(models.Model):
    title = models.CharField(max_length=120, unique=True)
