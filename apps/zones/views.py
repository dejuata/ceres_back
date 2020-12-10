from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from apps.zones.models import Zone
from apps.zones.serializers import ZoneSerializer
from apps.users.permission import IsAdminUser, IsManagerUser, IsFieldManagerUser


class ZoneViewSet(viewsets.ModelViewSet):
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer
    permission_classes = (IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        queryset = Zone.objects.filter(is_active=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        zona = Zone.objects.get(pk=kwargs['pk'])
        zona.is_active = False
        zona.save()
        return Response(status=status.HTTP_202_ACCEPTED)
