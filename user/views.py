from .serializers import SignUpSerializer
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, APIView
from rest_framework.request import Request
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


class SingUpView(generics.GenericAPIView):
    serializer_class = SignUpSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request: Request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            response = {
                "message": "User Created Successfully",
                "data": serializer.data,

            }

            return Response(data=response, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = []

    def post(self, request: Request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            response = {

                "messages": "Login Successefull",
                "token": user.auth_token.key
            }
            return Response(data=response, status=status.HTTP_200_OK)
        return Response(data={"messages": "invalid email or password"}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request: Request):
        content = {"user": str(request.user), "auth": str(request.auth)}
        return Response(data=content, status=status.HTTP_200_OK)