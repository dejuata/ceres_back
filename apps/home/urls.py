from django.urls import path
from apps.home.views import UserCountView, ActivitiesUser


urlpatterns = [
    path('', UserCountView.as_view(), name='home'),
    path('actividades/<pk>/', ActivitiesUser.as_view(), name='actividades-usuario'),
]
