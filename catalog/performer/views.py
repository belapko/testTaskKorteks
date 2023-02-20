from rest_framework import viewsets
from .serializers import PerformerModelSerializer
from .models import Performer


class PerformerViewSet(viewsets.ModelViewSet):
    serializer_class = PerformerModelSerializer
    queryset = Performer.objects.all()
