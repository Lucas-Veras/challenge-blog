from core.settings import SIMPLE_JWT
from drf_spectacular.utils import extend_schema
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.models.user import User
from users.serializers import (
    SuccessTokenObtainPairSerializer,
    UserSerializer,
    UserTokenObtainPairSerializer,
    UsuarioCreateSerializer,
)
from users.utils import get_future_datetime


@extend_schema(
    tags=["Auth"],
    request=UserTokenObtainPairSerializer,
    responses={
        "200": SuccessTokenObtainPairSerializer,
    },
)
class UserTokenObtainPairView(TokenObtainPairView):
    serializer_class = UserTokenObtainPairSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        data = response.data

        refresh_token = data.get("refresh")

        if refresh_token:

            cookie_expiration = get_future_datetime(
                SIMPLE_JWT["REFRESH_TOKEN_LIFETIME"],
            )

            response.set_cookie(
                key="refresh_token",
                value=refresh_token,
                expires=cookie_expiration,
                httponly=True,
                secure=True,
                samesite="Strict",
            )

        return response


@extend_schema(
    tags=["Auth"],
)
class UserTokenRefreshView(TokenRefreshView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        refresh_token = request.data.get("refresh")

        if not refresh_token:
            return Response(
                {
                    "success": False,
                    "message": "O Refresh token não foi encontrado.",
                },
                status=status.HTTP_401_UNAUTHORIZED,
            )

        request.data["refresh"] = refresh_token

        try:
            response = super().post(request, *args, **kwargs)
            return response
        except InvalidToken:
            return Response(
                {
                    "success": False,
                    "detail": "Token inválido!",
                },
                status=status.HTTP_401_UNAUTHORIZED,
            )


@extend_schema(tags=["Auth"])
class UsuarioCreateView(generics.CreateAPIView):
    serializer_class = UsuarioCreateSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return Response(
            {
                "success": True,
                "message": "Usuário criado com sucesso",
            },
            status=status.HTTP_201_CREATED,
        )


@extend_schema(tags=["Auth"])
class UserListView(generics.ListAPIView):
    queryset = User.objects.all().order_by("-id")
    serializer_class = UserSerializer


@extend_schema(tags=["Auth"])
class LogoutView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        response = Response()
        response.delete_cookie("refresh_token")
        response.data = {
            "success": True,
            "message": "Usuário deslogado com sucesso",
        }
        return response


@extend_schema(tags=["Auth"])
class UserLoggedView(APIView):
    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)
