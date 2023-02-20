from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from performer.views import PerformerViewSet
from albums.views import AlbumViewSet
from songs.views import SongViewSet

from .yasg import urlpatterns as doc_urls

# from rest_framework_swagger.views import get_swagger_view
#
# schema_view = get_swagger_view(title="Pastebin API")

router = DefaultRouter()
router.register('performers', PerformerViewSet)
router.register('albums', AlbumViewSet)
router.register('songs', SongViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # path('swagger/', schema_view),
]

urlpatterns += doc_urls
