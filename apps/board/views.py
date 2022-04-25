# Create your views here.
from argparse import Action
from re import A
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from .permissions import IsBoardAdmin, IsBoardModerator, IsUser, IsCreator
from .models import Board, ModeratorInvitaion, Thread, Post
from .serailizers import BoardSerializer, ModeratorInvitaionSerializer, ThreadSerailizer, PostSerailizer
from consts import actions


class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

    def get_permissions(self):
        permission_classes = [AllowAny]
        if self.action == actions.ACTION_CREATE:
            permission_classes = [IsAuthenticated]
        if self.action == actions.ACTION_PARTIAL_UPDATE or self.action == actions.ACTION_UPDATE:
            permission_classes = [IsAdminUser | IsBoardAdmin]
        if self.action == actions.ACTION_DESTROY:
            permission_classes = [IsAdminUser | IsBoardAdmin]

        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        request.data["created_by"] = request.user.id
        if "moderators" in request.data:
            request.data.pop("moderators")

        return super().create(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)


class ModeratorInviationViewSet(viewsets.ModelViewSet):
    queryset = ModeratorInvitaion.objects.all()
    serializer_class = ModeratorInvitaionSerializer

    http_method_names = ['get', 'put', 'patch']

    def get_permissions(self):
        permission_classes = [IsUser]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        id = "0"
        if self.request.user:
            id = str(self.request.user.id)
        self.queryset = self.queryset.filter(user_id=id)
        return super().get_queryset()


class ThreadViewSet(viewsets.ModelViewSet):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerailizer

    def get_permissions(self):
        permission_classes = [AllowAny]

        if self.action == actions.ACTION_CREATE:
            permission_classes = [IsBoardAdmin | IsBoardModerator]
        if self.action == actions.ACTION_UPDATE or self.action == actions.ACTION_PARTIAL_UPDATE or self.action == actions.ACTION_DESTROY:
            permission_classes = [IsBoardAdmin | IsBoardModerator | IsCreator]

        return [permission() for permission in permission_classes]
    
    def create(self, request, *args, **kwargs):
        self.request.data["created_by"] = request.user.id
        return super().create(request, *args, **kwargs)

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerailizer

    def get_permissions(self):
        permission_classes = [AllowAny]

        if self.action == actions.ACTION_CREATE:
            permission_classes = [IsBoardAdmin | IsBoardModerator]
        if self.action == actions.ACTION_UPDATE or self.action == actions.ACTION_PARTIAL_UPDATE or self.action == actions.ACTION_DESTROY:
            permission_classes = [IsBoardAdmin | IsBoardModerator | IsCreator]

        return [permission() for permission in permission_classes]
    
    def create(self, request, *args, **kwargs):
        self.request.data["created_by"] = request.user.id
        return super().create(request, *args, **kwargs)