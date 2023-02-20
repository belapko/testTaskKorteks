import datetime
from rest_framework import serializers
from .models import Album


class AlbumModelSerializer(serializers.ModelSerializer):
    def validate_year(self, value):
        if value < 1000 or value > datetime.date.today().year:
            raise serializers.ValidationError("Wrong year")
        return value

    class Meta:
        model = Album
        fields = ("performer", "year",)
