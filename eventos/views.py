from django.shortcuts import redirect, render
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from eventos.models import Evento

# Create your views here.
@login_required # type: ignore
def novo_evento(request):
    if request.method == "GET":
        return render(request, "novo_evento.html")
    elif request.method == "POST":
        criador = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
        nome = request.POST.get("nome")
        descricao = request.POST.get("descricao")
        data_inicio = request.POST.get("data_inicio")
        data_termino = request.POST.get("data_termino")
        carga_horaria = request.POST.get("carga_horaria")
        cor_principal = request.POST.get("cor_principal")
        cor_secundaria = request.POST.get("cor_principal")
        cor_fundo = request.POST.get("cor_fundo")
        logo = request.FILES.get("logo")

        evento = Evento(
            criador = request.user,
            nome = nome,
            descricao = descricao,
            data_inicio = data_inicio,
            data_termino = data_termino,
            carga_horaria = carga_horaria,
            cor_principal = cor_principal,
            cor_secundaria = cor_secundaria,
            cor_fundo = cor_fundo,
            logo = logo,
        )

        evento.save()

        messages.add_message(request, constants.SUCCESS, _("Evento cadastrado com sucesso"))
        return redirect(reverse("novo_evento"))