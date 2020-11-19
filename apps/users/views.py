from rest_framework import serializers, viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from apps.users.serializers import UserSerializer
from apps.users.models import User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
