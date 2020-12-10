from django.urls import path, include
from rest_framework import routers
from apps.worklogs.views import WorklogView

router = routers.DefaultRouter()
router.register(r'', WorklogView)

urlpatterns = [
    path('', include(router.urls))
]
