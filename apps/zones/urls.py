from django.urls import path, include
from rest_framework import routers
from apps.zones.views import ZoneViewSet

router = routers.DefaultRouter()
router.register(r'', ZoneViewSet)

urlpatterns = [
    path('', include(router.urls))
]
