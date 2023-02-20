from rest_framework import viewsets
from .models import Album
from .serializers import AlbumModelSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    serializer_class = AlbumModelSerializer
    queryset = Album.objects.all()
