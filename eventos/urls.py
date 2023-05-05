from django.urls import path
from . import views

urlpatterns = [
    path('novo_evento/', views.novo_evento, name="novo_evento"), # type: ignore
    path("gerenciar_evento/", views.gerenciar_evento, name="gerenciar_evento") # type: ignore
]