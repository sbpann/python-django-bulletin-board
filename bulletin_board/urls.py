from django.urls import include, path
from apps.user.views import UserViewSet, UserAvatarView
from apps.board.views import BoardViewSet, ModeratorInviationViewSet, PostViewSet, ThreadViewSet
from apps.rest_auth.views import LoginView
from rest_framework import routers


router = routers.DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'boards/moderator_invitaions', ModeratorInviationViewSet)
router.register(r'boards', BoardViewSet)
router.register(r'posts', PostViewSet)
router.register(r'threads', ThreadViewSet)

urlpatterns = [
    path('auth/login', LoginView.as_view()),
    path('users/<int:user_id>/avatar', UserAvatarView.as_view()),
    path('', include(router.urls))
]
