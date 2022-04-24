from email.mime import base
from rest_framework import permissions

class IsBoardAdmin(permissions.BasePermission):
    pass

class IsBoardModerator(permissions.BasePermission):
    pass