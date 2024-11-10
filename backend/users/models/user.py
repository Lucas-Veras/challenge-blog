from uuid import uuid4

from django.conf import settings
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _
from users.managers import UserManager

from .person import Person


def upload_to(instance, filename):
    uuid = uuid4()
    uuid = str(uuid).replace("-", "")
    extention = filename.split(".")[-1]

    return f"{settings.AVATAR_URL}/{uuid}.{extention}"


class User(AbstractUser):
    email = models.EmailField(
        verbose_name="Email",
        max_length=300,
        unique=True,
        null=False,
        blank=False,
        error_messages={"unique": "Já existe um usuário com esse email."},
    )

    person = models.ForeignKey(
        to=Person,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="usuarios",
        editable=True,
    )

    avatar = models.FileField(
        verbose_name="Avatar",
        upload_to=upload_to,
        blank=True,
        null=True,
        unique=False,
    )

    groups = models.ManyToManyField(
        to=Group,
        related_name="user_groups",
        blank=True,
    )

    @property
    def name(self):
        return self.person.name.split(" ")[0]

    username = None
    first_name = None
    last_name = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        db_table = "user"

    def __str__(self) -> str:
        return f"{self.email} - {self.person}"
