from django.contrib.auth.hashers import make_password
from django.db import migrations
from users.constants import GroupUserEnum


def populate(apps, schema_editor):
    users = [
        {
            "name": "lucas",
            "email": "lucas@gmail.com",
            "password": "#Senha123",
            "is_superuser": False,
            "is_staff": False,
        },
        {
            "name": "maria",
            "email": "maria@gmail.com",
            "password": "#Senha123",
            "is_superuser": False,
            "is_staff": False,
        },
        {
            "name": "joao",
            "email": "joao@gmail.com",
            "password": "#Senha123",
            "is_superuser": False,
            "is_staff": False,
        },
        {
            "name": "admin",
            "email": "admin@gmail.com",
            "password": "#Senha123",
            "is_superuser": True,
            "is_staff": True,
        },
    ]

    model_person = apps.get_model("users", "Person")
    model_user = apps.get_model("users", "User")
    model_group = apps.get_model("auth", "Group")

    for user_data in users:
        person_instance, created = model_person.objects.get_or_create(
            name=user_data["name"],
        )
        common_user, created = model_group.objects.get_or_create(
            name=GroupUserEnum.COMMON_USER,
        )
        user_instance, created = model_user.objects.get_or_create(
            email=user_data["email"],
            is_superuser=user_data["is_superuser"],
            is_staff=user_data["is_staff"],
            person=person_instance,
            password=make_password(user_data["password"]),
        )
        user_instance.groups.add(common_user)


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_alter_person_name"),
    ]

    operations = [
        migrations.RunPython(
            code=populate,
            atomic=True,
        )
    ]
