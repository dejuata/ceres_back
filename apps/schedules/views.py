from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from apps.schedules.models import Schedule
from rest_framework.response import Response
from rest_framework import status
from apps.schedules.serializers import ScheduleSerializer


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = (IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        queryset = Schedule.objects.filter(is_active=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        actividad = Schedule.objects.get(pk=kwargs['pk'])
        actividad.is_active = False
        actividad.save()
        return Response(status=status.HTTP_202_ACCEPTED)
