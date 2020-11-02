from django.conf import settings
from django.contrib.auth import authenticate
from datetime import datetime, timedelta
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.users.models import User
from apps.gateway.models import Jwt
from apps.gateway.serializers import LoginSerializer, RegisterSerializer

import random
import string
import jwt

def get_random(length):
    ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def get_access_token(payload):
    return jwt.encode(
        {"exp": datetime.now() + timedelta(minutes=5), **payload},
        settings.SECRET_KEY,
        algorithm="HS256"
    )

def get_refresh_token():
    return jwt.encode(
        {"exp": datetime.now() + timedelta(days=365), "data": get_random(10)},
        settings.SECRET_KEY,
        algorithm="HS256"
    )


class LoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            username=serializer.validated_data['email'],
            password=serializer.validated_data['password']
        )

        if not user:
            return Response({"error": "Invalid email or password"}, status=status.HTTP_400_BAD_REQUEST)

        access = get_access_token({"user_id": user.id})
        refresh = get_refresh_token()

        Jwt.objects.create(
            user_id=user.id, access=access, refresh=refresh
        )

        return Response({"access": access, "refresh": refresh})


class RegisterView(APIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        User.objects.create_user(**serializer.validated_data)

        return Response({"success": "User created successfully"}, status=status.HTTP_201_CREATED)
