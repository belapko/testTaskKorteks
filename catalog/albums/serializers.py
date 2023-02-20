import datetime
from rest_framework import serializers

from .models import Album
from songs.serializers import SongModelSerializer


class AlbumModelSerializer(serializers.ModelSerializer):
    songs_list = SongModelSerializer(many=True, read_only=True)

    def validate_year(self, value):
        if value < 1000 or value > datetime.date.today().year:
            raise serializers.ValidationError("Wrong year")
        return value

    class Meta:
        model = Album
        fields = ("title", "performer", "year", "songs_list",)
