from django.db import models


class Person(models.Model):
    name = models.CharField(
        verbose_name="Nome",
        max_length=200,
        unique=False,
        null=False,
        blank=False,
    )

    class Meta:
        db_table = "person"
