from email.mime import base
from rest_framework import permissions

class IsBoardAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.created_by == request.user

class IsUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

class IsBoardModerator(permissions.BasePermission):
    pass