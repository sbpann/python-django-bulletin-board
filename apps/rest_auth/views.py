from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from services import auth_service

class LoginView(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def post(self, request, format=None):
        username = request.data.get("username")
        password = request.data.get("password")
        token = auth_service.Login(username=username, password=password)
        if token is None:
            return Response({"message": "username or password is not correct"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"token": token}, status = status.HTTP_200_OK)