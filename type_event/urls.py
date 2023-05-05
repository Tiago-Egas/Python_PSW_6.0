from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),  # type: ignore
    path('usuarios/', include('usuarios.urls')),  # type: ignore
    path('eventos/', include('eventos.urls')),  # type: ignore
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
