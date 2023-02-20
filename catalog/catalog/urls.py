from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from performer.views import PerformerViewSet

router = DefaultRouter()
router.register('performers', PerformerViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
