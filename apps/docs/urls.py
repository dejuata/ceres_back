from django.urls import path
from django.views.generic import TemplateView
# from rest_framework.schemas import get_schema_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="Ceres App",
        default_version='v1',
        description="API PWA",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="juan.david.pino.reyes@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]
# path('openapi', get_schema_view(
#         title="Ceres App",
#         description="API PWA",
#         version="1.0.0"),
#         name='openapi-schema'
#     )
