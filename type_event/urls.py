from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),  # type: ignore
    path('usuarios/', include('usuarios.urls')),  # type: ignore
    path('eventos/', include('eventos.urls')),  # type: ignore
]
