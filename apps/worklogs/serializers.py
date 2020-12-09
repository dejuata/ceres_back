from rest_framework import serializers
from apps.worklogs.models import Worklog


class WorlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worklog
        fields = (
            'id',
            'date',
            'description',
            'file',
            'actividad',
            'name_operator',
            'codigo_zona',
            'nombre_labor',
            'state',
            'lat',
            'lng'
        )
