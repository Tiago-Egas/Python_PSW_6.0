from django.urls import path
from . import views

urlpatterns = [
    path("novo_evento/", views.novo_evento, name="novo_evento"),  # type: ignore
    path("gerenciar_evento/", views.gerenciar_evento, name="gerenciar_evento"),  # type: ignore
    path("inscrever_evento/<int:id>/", views.inscrever_evento, name="inscrever_evento"),  # type: ignore
    path('participantes_evento/<int:id>', views.participantes_evento, name="participantes_evento")  # type: ignore
]
