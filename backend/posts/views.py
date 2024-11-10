from drf_spectacular.utils import extend_schema
from posts.models.post import Post
from posts.serializers import PostSerializer
from rest_framework import filters, generics
from rest_framework.permissions import AllowAny


@extend_schema(tags=["Posts"])
class PostView(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = [
        "title",
        "author__person__name",
    ]

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
