from consts import actions
from .permissions import IsSelf
from .models import User
from .serailizers import UserSerializer
from rest_framework import viewsets, status
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework.response import Response
from services import auth_service, user_service

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == actions.ACTION_LIST:
            permission_classes = [AllowAny]
        elif self.action == actions.ACTION_RETRIEVE:
            permission_classes = [IsAdminUser | IsSelf]
        elif self.action == actions.ACTION_UPDATE or self.action == actions.ACTION_PARTIAL_UPDATE:
            permission_classes = [IsSelf]
        elif self.action == actions.ACTION_DESTROY:
            permission_classes = [IsAdminUser | IsSelf]
        else:
            permission_classes = [AllowAny]
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