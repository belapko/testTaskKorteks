from rest_framework import serializers
from .models import Song


class SongModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ("title", "serial_number", "album")
