from tkinter.messagebox import NO
from django.urls import include, path
from apps.user.views import UserViewSet
from apps.board.views import BoardViewSet, ModeratorInviationViewSet
from apps.rest_auth.views import LoginView
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'boards/moderator_invitaions', ModeratorInviationViewSet)
router.register(r'boards', BoardViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/login', LoginView.as_view())
]
