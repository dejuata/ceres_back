from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from apps.labors.models import Labor
from apps.labors.serializers import LaborSerializer


class LaborViewSet(viewsets.ModelViewSet):
    queryset = Labor.objects.all()
    serializer_class = LaborSerializer
    permission_classes = (AllowAny,)
