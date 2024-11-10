from django.db import models


class Post(models.Model):
    title = models.CharField(
        verbose_name="title",
        max_length=200,
        unique=False,
        null=False,
        blank=False,
    )

    content = models.TextField(
        verbose_name="content",
        unique=False,
        null=False,
        blank=False,
        max_length=10000,
    )

    author = models.ForeignKey(
        "users.User",
        on_delete=models.PROTECT,
        verbose_name="author",
        related_name="posts",
    )

    created_at = models.DateTimeField(
        verbose_name="created_at",
        auto_now_add=True,
    )

    class Meta:
        db_table = "post"
