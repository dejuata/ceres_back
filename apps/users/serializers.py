from rest_framework import serializers
from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'id_card')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 6}}
