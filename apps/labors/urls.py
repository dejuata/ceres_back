from django.urls import path, include
from rest_framework import routers
from apps.labors.views import LaborViewSet

router = routers.DefaultRouter()
router.register(r'', LaborViewSet)

urlpatterns = [
    path('', include(router.urls))
]
