from rest_framework import serializers
from apps.zones.models import Zone


class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zone
        fields = ('id', 'id_zone', 'soil_type', 'size', 'state', 'lat', 'lng')
