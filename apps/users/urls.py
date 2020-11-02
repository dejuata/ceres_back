from django.urls import path, include
from rest_framework import routers
from apps.users.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'', UserViewSet)

urlpatterns = [
    path('', include(router.urls))
]
