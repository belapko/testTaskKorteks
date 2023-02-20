from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from performer.views import PerformerViewSet
from albums.views import AlbumViewSet
from songs.views import SongViewSet

router = DefaultRouter()
router.register('performers', PerformerViewSet)
router.register('albums', AlbumViewSet)
router.register('songs', SongViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
