from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from apps.labors.models import Labor
from apps.labors.serializers import LaborSerializer


class LaborViewSet(viewsets.ModelViewSet):
    queryset = Labor.objects.all()
    serializer_class = LaborSerializer
    permission_classes = (IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        queryset = Labor.objects.filter(is_active=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        labor = Labor.objects.get(pk=kwargs['pk'])
        labor.is_active = False
        labor.save()
        return Response(status=status.HTTP_202_ACCEPTED)
