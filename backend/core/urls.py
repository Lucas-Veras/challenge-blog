from core.config.swagger import api_doc
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from posts.urls import posts_urls
from users.urls import users_urls

api_path = [
    path("auth/", include(users_urls)),
    path("posts/", include(posts_urls)),
]


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(api_path)),
    path("api/doc/", include(api_doc)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
