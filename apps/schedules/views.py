from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from apps.schedules.models import Schedule
from apps.schedules.serializers import ScheduleSerializer


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = (AllowAny,)
