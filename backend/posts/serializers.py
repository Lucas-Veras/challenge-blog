from posts.models.post import Post
from rest_framework import serializers


class PostBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "content",
        )


class PostSerializer(PostBaseSerializer):
    author = serializers.CharField(source="author.username", read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    class Meta(PostBaseSerializer.Meta):
        model = Post
        fields = PostBaseSerializer.Meta.fields + (
            "author",
            "created_at",
        )


class PostCreateSerializer(PostBaseSerializer):
    author = serializers.CharField(source="author.username", read_only=True)
    created_at = serializers.DateTimeField(
        read_only=True,
        format="%d/%m/%Y %H:%M:%S",
    )

    class Meta(PostBaseSerializer.Meta):
        model = Post
        fields = PostBaseSerializer.Meta.fields + (
            "author",
            "created_at",
        )
