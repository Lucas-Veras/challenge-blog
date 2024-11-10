from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import PostView

router = DefaultRouter()

posts_urls = [
    path(
        "",
        PostView.as_view(),
        name="list-posts",
    ),
]


posts_urls += router.urls
