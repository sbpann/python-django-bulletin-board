from consts import actions
from .permissions import IsSelf
from .models import User
from .serailizers import UserSerializer
from rest_framework import viewsets, status
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == actions.ACTION_LIST:
            permission_classes = [IsAuthenticated]
        elif self.action == actions.ACTION_RETRIEVE:
            permission_classes = [IsAdminUser | IsSelf]
        elif self.action == actions.ACTION_UPDATE or self.action == actions.ACTION_PARTIAL_UPDATE:
            permission_classes = [IsSelf]
        elif self.action == actions.ACTION_DESTROY:
            permission_classes = [IsAdminUser | IsSelf]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]