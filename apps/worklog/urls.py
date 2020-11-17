from django.urls import path
from apps.worklog.views import WorklogView

urlpatterns = [
    path('', WorklogView.as_view())
]