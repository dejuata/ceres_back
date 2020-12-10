from django.urls import path
from apps.home.views import UserCountView, ActivitiesUser, ActividadesOperarioView, ActividadesZonaView, ActividadesHechasOperarioView, ActividadesNoHechasOperarioView, ActividadesHechasZonaView, ActividadesNoHechasZonaView


urlpatterns = [
    path('', UserCountView.as_view(), name='home'),
    path('actividades/<pk>/', ActivitiesUser.as_view(), name='actividades-usuario'),
    path('actividades_operario/', ActividadesOperarioView.as_view(), name='actividades_operario-usuario'),
    path('actividades_hechas_operario/', ActividadesHechasOperarioView.as_view(), name='actividades_hechas_operario-usuario'),
    path('actividades_no_hechas_operario/', ActividadesNoHechasOperarioView.as_view(), name='actividades_no_hechas_operario-usuario'),
    path('actividades_zona/', ActividadesZonaView.as_view(), name='actividades_zona-usuario'),
    path('actividades_hechas_zona/', ActividadesHechasZonaView.as_view(), name='actividades_hechas_zona-usuario'),
    path('actividades_no_hechas_zona/', ActividadesNoHechasZonaView.as_view(), name='actividades_no_hechas_zona-usuario'),
]
