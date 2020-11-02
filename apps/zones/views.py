from rest_framework import viewsets
from apps.zones.models import Zone
from apps.zones.serializers import ZoneSerializer


class ZoneViewSet(viewsets.ModelViewSet):
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer
