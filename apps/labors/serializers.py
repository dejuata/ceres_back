from rest_framework import serializers
from apps.labors.models import Labor


class LaborSerializer(serializers.ModelSerializer):
    class Meta:
        model = Labor
        fields = ('id', 'name', 'description', 'labor_type')
