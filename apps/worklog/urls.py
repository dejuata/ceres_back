from django.urls import path, include
from rest_framework import routers
from apps.worklog.views import WorklogView

router = routers.DefaultRouter()
router.register(r'', WorklogView)

urlpatterns = [
    path('', include(router.urls))
]
