from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from apps.zones.models import Zone
from apps.zones.serializers import ZoneSerializer
from apps.users.permission import IsAdminUser, IsManagerUser, IsFieldManagerUser


class ZoneViewSet(viewsets.ModelViewSet):
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer
    permission_classes = (AllowAny, IsAdminUser, IsManagerUser, IsFieldManagerUser)
