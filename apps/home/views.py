from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from apps.authentication.models import User
from apps.schedules.models import Schedule
from apps.labors.models import Labor
from apps.zones.models import Zone

class UserCountView(APIView):
    """
    A view that returns the count of active users.
    """
    renderer_classes = (JSONRenderer, )

    def get(self, request, format=None):
        actividades = Schedule.objects.count()
        labores = Labor.objects.count()
        zonas = Zone.objects.count()
        content = {
            'actividades': actividades,
            'labores': labores,
            'zonas': zonas
        }
        return Response(content)
