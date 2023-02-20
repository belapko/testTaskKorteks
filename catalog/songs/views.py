from rest_framework import viewsets
from .serializers import SongModelSerializer
from .models import Song


class SongViewSet(viewsets.ModelViewSet):
    serializer_class = SongModelSerializer
    queryset = Song.objects.all()
