from django.urls import path
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny

@permission_classes([AllowAny])
def schemaView():
    return TemplateView.as_view(
        template_name='redoc.html',
        extra_context={'schema_url': 'openapi-schema'}
    )

urlpatterns = [
    path('', schemaView(), name='redoc'),
    path('openapi', get_schema_view(
        title="Ceres App",
        description="API PWA",
        version="1.0.0"),
        name='openapi-schema'
    )
]
