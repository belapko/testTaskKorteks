from django.db import models
from albums.models import Album


class Song(models.Model):
    title = models.CharField(max_length=120)
    album = models.ManyToManyField(Album, related_name='songs_list')
    serial_number = models.IntegerField()
