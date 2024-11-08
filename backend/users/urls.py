from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    LogoutView,
    UserListView,
    UserTokenObtainPairView,
    UserTokenRefreshView,
    UsuarioCreateView,
)

router = DefaultRouter()

users_urls = [
    path(
        "register/",
        UsuarioCreateView.as_view(),
        name="user-register",
    ),
    path(
        "login/",
        UserTokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path(
        "token/refresh/",
        UserTokenRefreshView.as_view(),
        name="token_refresh",
    ),
    path("logout/", LogoutView.as_view()),
    path("users/", UserListView.as_view(), name="user-list"),
]


users_urls += router.urls
