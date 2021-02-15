from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from blog import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('article.urls')),
    path('api/', include('api.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
