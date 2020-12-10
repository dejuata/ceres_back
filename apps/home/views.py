from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from apps.authentication.models import User
from apps.schedules.models import Schedule
from apps.labors.models import Labor
from apps.zones.models import Zone
from apps.worklogs.models import Worklog
from apps.home.serializers import ActividadSerializer
import json
from datetime import datetime


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

class ActividadesOperarioView(APIView):
    """
    A view that returns the count of total activities by date.
    """
    renderer_classes = (JSONRenderer, )

    def get(self, request, format=None):
        operarios = User.objects.filter(role=4)
        actividades_result = []
        for oper in operarios:
            actividad_operario = {
                'label': oper.first_name + ' ' + oper.last_name,
                'y': Schedule.objects.filter(operator=oper).count()
            }
            actividades_result.append(actividad_operario)
        content = {
            'data': actividades_result,
        }
        return Response(actividades_result)

    def post(self, request, format=None):
        operarios = User.objects.filter(role=4)
        data = request.data
        ahora = datetime.now(tz=None).date()
        if data:
            start = data.get('start', ahora) if data.get('start', '') != '' else ahora
            end = data.get('end', ahora) if data.get('end', '') != '' else ahora
            zone = data.get('zone', '')
        else:
            start = ahora
            end = ahora
            zone = ''
        actividades_result = []

        for oper in operarios:
            eventos = Schedule.objects.filter(operator=oper, schedule_date__gte=start, schedule_date__lte=end)
            zona = Zone.objects.filter(id=zone).first() if zone else False
            if zona: eventos = eventos.filter(zone=zona)
            actividad_operario = {
                'label': oper.first_name + ' ' + oper.last_name,
                'y': eventos.count()
            }
            actividades_result.append(actividad_operario)
        return Response(actividades_result)

class ActividadesHechasOperarioView(APIView):
    """
    A view that returns the count of done activities by date.
    """
    renderer_classes = (JSONRenderer, )

    def post(self, request, format=None):
        operarios = User.objects.filter(role=4)
        data = request.data
        ahora = datetime.now(tz=None).date()
        if data:
            start = data.get('start', ahora) if data.get('start', '') != '' else ahora
            end = data.get('end', ahora) if data.get('end', '') != '' else ahora
            zone = data.get('zone', '')
        else:
            start = ahora
            end = ahora
            zone = ''
        actividades_result = []

        for oper in operarios:
            eventos = Schedule.objects.filter(operator=oper, schedule_date__gte=start, schedule_date__lte=end)
            zona = Zone.objects.filter(id=zone).first() if zone else False
            if zona: eventos = eventos.filter(zone=zona)
            contador = 0
            for ev in eventos:
                if Worklog.objects.filter(actividad=ev).exists():
                    contador = contador+1 
            actividad_operario = {
                'label': oper.first_name + ' ' + oper.last_name,
                'y': contador
            }
            actividades_result.append(actividad_operario)
        return Response(actividades_result)

class ActividadesNoHechasOperarioView(APIView):
    """
    A view that returns the count of done activities by date.
    """
    renderer_classes = (JSONRenderer, )

    def post(self, request, format=None):
        operarios = User.objects.filter(role=4)
        data = request.data
        ahora = datetime.now(tz=None).date()
        if data:
            start = data.get('start', ahora) if data.get('start', '') != '' else ahora
            end = data.get('end', ahora) if data.get('end', '') != '' else ahora
            zone = data.get('zone', '')
        else:
            start = ahora
            end = ahora
            zone = ''
        actividades_result = []

        for oper in operarios:
            eventos = Schedule.objects.filter(operator=oper, schedule_date__gte=start, schedule_date__lte=end)
            zona = Zone.objects.filter(id=zone).first() if zone else False
            if zona: eventos = eventos.filter(zone=zona)
            contador = 0
            for ev in eventos:
                if not Worklog.objects.filter(actividad=ev).exists():
                    contador = contador+1 
            actividad_operario = {
                'label': oper.first_name + ' ' + oper.last_name,
                'y': contador
            }
            actividades_result.append(actividad_operario)
        return Response(actividades_result)

class ActividadesZonaView(APIView):
    """
    A view that returns the count of active users.
    """
    renderer_classes = (JSONRenderer, )

    def post(self, request, format=None):
        zonas = Zone.objects.filter(is_active=True)
        data = request.data
        ahora = datetime.now(tz=None).date()
        if data:
            start = data.get('start', ahora) if data.get('start', '') != '' else ahora
            end = data.get('end', ahora) if data.get('end', '') != '' else ahora
        else:
            start = ahora
            end = ahora

        actividades_result = []

        for zona in zonas:
            eventos = Schedule.objects.filter(zone=zona, schedule_date__gte=start, schedule_date__lte=end)
            actividad_operario = {
                'name': zona.id_zone,
                'y': eventos.count()
            }
            actividades_result.append(actividad_operario)

        return Response(actividades_result)

class ActividadesHechasZonaView(APIView):
    """
    A view that returns the count of active users.
    """
    renderer_classes = (JSONRenderer, )

    def post(self, request, format=None):
        zonas = Zone.objects.filter(is_active=True)
        data = request.data
        ahora = datetime.now(tz=None).date()
        if data:
            start = data.get('start', ahora) if data.get('start', '') != '' else ahora
            end = data.get('end', ahora) if data.get('end', '') != '' else ahora
        else:
            start = ahora
            end = ahora

        actividades_result = []

        for zona in zonas:
            eventos = Schedule.objects.filter(zone=zona, schedule_date__gte=start, schedule_date__lte=end)
            contador = 0
            for ev in eventos:
                if Worklog.objects.filter(actividad=ev).exists():
                    contador = contador+1
            actividad_operario = {
                'name': zona.id_zone,
                'y': contador
            }
            actividades_result.append(actividad_operario)

        return Response(actividades_result)

class ActividadesNoHechasZonaView(APIView):
    """
    A view that returns the count of active users.
    """
    renderer_classes = (JSONRenderer, )

    def post(self, request, format=None):
        zonas = Zone.objects.filter(is_active=True)
        data = request.data
        ahora = datetime.now(tz=None).date()
        if data:
            start = data.get('start', ahora) if data.get('start', '') != '' else ahora
            end = data.get('end', ahora) if data.get('end', '') != '' else ahora
        else:
            start = ahora
            end = ahora

        actividades_result = []

        for zona in zonas:
            eventos = Schedule.objects.filter(zone=zona, schedule_date__gte=start, schedule_date__lte=end)
            contador = 0
            for ev in eventos:
                print(ev)
                if not Worklog.objects.filter(actividad=ev).exists():
                    print("--Contador--", contador)
                    contador = contador+1
            actividad_operario = {
                'name': zona.id_zone,
                'y': contador
            }
            actividades_result.append(actividad_operario)

        return Response(actividades_result)