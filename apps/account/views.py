from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from apps.account.serializer import RegisterSerializer
from apps.users.serializers import UserSerializer
from apps.users.models import User


class RegisterView(APIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        User.objects.create_user(**serializer.validated_data)

        return Response({"success": "User created successfully"}, status=status.HTTP_201_CREATED)
