from django.urls import path
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('', TemplateView.as_view(template_name='redoc.html', extra_context={'schema_url': 'openapi-schema'}), name='redoc'),
    path('openapi', get_schema_view(
        title="Ceres App",
        description="API PWA",
        version="1.0.0"),
        name='openapi-schema'),
]
