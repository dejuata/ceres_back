from rest_framework import viewsets
from apps.labors.models import Labor
from apps.labors.serializers import LaborSerializer


class LaborViewSet(viewsets.ModelViewSet):
    queryset = Labor.objects.all()
    serializer_class = LaborSerializer
