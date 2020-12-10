from rest_framework import serializers
from apps.schedules.models import Schedule


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = (
            'id',
            'schedule_date',
            'start_hour',
            'final_hour',
            'observation',
            'zone',
            'labor',
            'operator',
            'name_operator',
            'codigo_zona',
            'nombre_labor'
        )
