from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from services import auth_service, user_service


class LoginView(APIView):
    def post(self, request, format=None):
        username = request.data.get("username")
        password = request.data.get("password")
        user = user_service.FindByUsername(username=username)
        if user_service.ValidatePassword(user, password):
            return Response({"message": "username or password is not correct"}, status=status.HTTP_400_BAD_REQUEST)
        token = auth_service.Login(user)
        return Response({"token": token}, status=status.HTTP_200_OK)
