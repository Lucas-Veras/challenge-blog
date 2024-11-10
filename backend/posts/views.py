from drf_spectacular.utils import extend_schema
from posts.models.post import Post
from posts.serializers import PostCreateSerializer, PostSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny


@extend_schema(tags=["Posts"])
class PostView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return super().get_permissions()

    def get_serializer(self, *args, **kwargs):
        if self.request.method == "POST":
            return PostCreateSerializer(*args, **kwargs)
        return super().get_serializer(*args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
