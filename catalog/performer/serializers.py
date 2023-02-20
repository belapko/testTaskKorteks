from rest_framework import serializers
from .models import Performer


class PerformerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performer
        fields = ("title", )
