from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from apps.authentication.models import User
from apps.schedules.models import Schedule
from apps.labors.models import Labor
from apps.zones.models import Zone
from apps.home.serializers import ActividadSerializer
import json


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


class ActivitiesUser(APIView):
    """
    Retornar las actividades asignadas a un usuario
    """
    renderer_classes = (JSONRenderer, )

    def get(self, request, pk, format=None):
        try:
            actividades = ActividadSerializer(
                Schedule.objects.filter(operator=pk), many=True).data
            return Response({'actividades': actividades})
        except Exception:
            return Response({'message': 'No hay actividades para este operador'})
