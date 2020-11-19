from django.urls import path
from apps.home.views import UserCountView


urlpatterns = [
    path('', UserCountView.as_view(), name='home'),
]
