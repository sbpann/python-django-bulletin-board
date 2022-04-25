from http.client import UNAUTHORIZED
from rest_framework import permissions, exceptions
from .models import Board, Thread, Post

Unauthenticated = exceptions.AuthenticationFailed('please log in or register user.')

class IsBoardAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user is None or not request.user.is_authenticated:
            raise Unauthenticated 
        if "thread" in request.data:
            thread = Thread.objects.get(id=request.data.get("thread"))
            return request.user == thread.board.created_by
        if "board" in request.data:
            board = Board.objects.get(id=request.data.get("board"))
            return request.user == board.created_by
        return super().has_permission(request, view)

    def has_object_permission(self, request, view, obj):
        if isinstance(obj, Board):
            return request.user == obj.created_by
        if isinstance(obj, Thread):
            return request.user == obj.board.created_by
        if isinstance(obj, Post):
            return request.user == obj.thread.board.created_by

class IsUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user is None or not request.user.is_authenticated:
            raise Unauthenticated 
        return super().has_permission(request, view)

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

class IsCreator(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user is None or not request.user.is_authenticated:
            raise Unauthenticated 
        return super().has_permission(request, view)

    def has_object_permission(self, request, view, obj):
        return obj.created_by == request.user

class IsBoardModerator(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user is None or not request.user.is_authenticated:
            raise Unauthenticated 
        if "thread" in request.data:
            thread = Thread.objects.get(id=request.data.get("thread"))
            return request.user in thread.board.moderators.all()
        if "board" in request.data:
            board = Board.objects.get(id=request.data.get("board"))
            return request.user in board.moderators.all()
        return super().has_permission(request, view)

    def has_object_permission(self, request, view, obj):
        if isinstance(obj, Board):
            return request.user in obj.moderators.all()
        if isinstance(obj, Thread):
            return request.user in obj.board.moderators.all()
        if isinstance(obj, Post):
            return request.user in obj.thread.board.moderators.all()
