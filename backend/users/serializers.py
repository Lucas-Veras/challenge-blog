from datetime import datetime

from core.settings import SIMPLE_JWT
from django.contrib.auth.models import Group
from django.contrib.auth.password_validation import validate_password
from django.db import transaction
from rest_framework import serializers
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.utils import datetime_to_epoch
from users.constants import GroupUserEnum
from users.models.person import Person
from users.models.user import User
from users.utils import get_future_datetime


class SuccessTokenObtainPairSerializer(serializers.Serializer):
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)


class UserTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user: User):
        token = super().get_token(user)
        token["email"] = user.email
        return token

    def validate(self, attrs):
        email = attrs.get("email")
        detail = {
            "success": False,
            "message": "Usuário e/ou senha incorreto(s)",
        }
        self.error_messages["no_active_account"] = detail
        try:
            user: User = User.objects.get(email=email)

            access_exp = get_future_datetime(
                SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"],
            )
            data = super().validate(attrs)

            roles = list(user.groups.all().values("name"))
            data["roles"] = roles
            data["exp"] = datetime_to_epoch(access_exp)
            return data
        except User.DoesNotExist:
            raise NotFound(
                detail={
                    "success": False,
                    "message": "Usuário e/ou senha incorreto(s)",
                },
                code=HTTP_401_UNAUTHORIZED,
            )


class UsuarioCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        required=True,
        write_only=True,
        validators=[validate_password],
    )

    name = serializers.CharField(
        required=True,
        write_only=True,
    )

    class Meta:
        model = User
        fields = (
            "id",
            "name",
            "email",
            "password",
        )

    def create(self, validated_data):
        with transaction.atomic():
            common_user, created = Group.objects.get_or_create(
                name=GroupUserEnum.COMMON_USER
            )
            user = User.objects.create(
                email=validated_data["email"],
            )

            person = Person.objects.create(
                name=validated_data["name"],
            )
            user.set_password(validated_data["password"])
            user.groups.add(common_user)
            user.person = person
            user.save()
            return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "name",
        )
