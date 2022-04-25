from .models import User
from .serailizers import UserSerializer
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from services import auth_service, user_service
from django_gravatar.helpers import get_gravatar_url, has_gravatar, get_gravatar_profile_url, calculate_gravatar_hash

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    def get_permissions(self):
        permission_classes = [AllowAny] # TODO: For development purposr only don't use in production
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        token = auth_service.Login(user_service.FindByUsername(serializer.data.get("username")))

        out = dict(serializer.data)
        out["token"] = token
        return Response(out, status=status.HTTP_201_CREATED, headers=headers)

class UserAvatarView(APIView):
    def get(self, request, *args, **kwargs):
        user = user_service.Find(str(kwargs.get("user_id")))
        if user is None or user.email == "" or not has_gravatar(user.email):
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"url": get_gravatar_url(user.email, size=150)}, status=status.HTTP_200_OK)
