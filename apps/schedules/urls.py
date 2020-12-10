from django.urls import path, include
from rest_framework import routers
from apps.schedules.views import ScheduleViewSet

router = routers.DefaultRouter()
router.register(r'', ScheduleViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
