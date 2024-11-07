from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core.config.swagger import api_doc

api_path =[
    # path("auth/", include("authentication.urls")),
    #path("user/", include("user.urls")),   
]


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(api_path)),
    path("api/doc/", include(api_doc)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)