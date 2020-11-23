from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from apps.account.serializer import RegisterSerializer, LoginSerializer
from apps.users.models import User


class RegisterView(APIView):
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            serializer.save()
            status_code = status.HTTP_200_OK
            email = request.data['email']
            password = request.data['password']
            user = authenticate(email=email, password=password)
            refresh = RefreshToken.for_user(user)
            refresh_token = str(refresh)
            access_token = str(refresh.access_token)

            response = {
                'success': True,
                'status': status_code,
                'message': 'User successfully registered!',
                'token': access_token,
                'refresh': refresh_token,
                'authenticatedUser': serializer.data
            }

            return Response(response, status=status_code)


class LoginView(APIView):
    serializer_class = LoginSerializer
    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_200_OK
            response = {
                'success': True,
                'status': status_code,
                'message': 'User logged in successfully',
                'token': serializer.data['access'],
                'refresh': serializer.data['refresh'],
                'authenticatedUser': {
                    'email': serializer.data['email'],
                    'role': serializer.data['role'],
                    'name': serializer.data['name']
                }
            }

            return Response(response, status=status_code)
