from rest_framework import serializers
from apps.users.models import User, UserProfile
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User()
        fields = ('id', 'email', 'password', 'first_name')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 6}}


class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=get_user_model().objects.all())

    class Meta:
        model = UserProfile
        fields = ('__all__')

"""
class UserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    first_name = serializers.CharField()

    def create(self, validate_data):
        instance = User()
        instance.email = validate_data.get('email')
        instance.set_password(validate_data.get('password'))
        instance.first_name = validate_data.get('first_name')
        instance.save()
        return instance
"""
