from django.shortcuts import HttpResponse, redirect, render, get_object_or_404
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from eventos.models import Evento  # type: ignore

# Create your views here.


@login_required  # type: ignore
def novo_evento(request):
    if request.method == "GET":
        return render(request, "novo_evento.html")

    if request.method == "POST":
        criador = models.ForeignKey(
            User, on_delete=models.CASCADE, null=True, blank=True)
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
            criador=request.user,
            nome=nome,
            descricao=descricao,
            data_inicio=data_inicio,
            data_termino=data_termino,
            carga_horaria=carga_horaria,
            cor_principal=cor_principal,
            cor_secundaria=cor_secundaria,
            cor_fundo=cor_fundo,
            logo=logo,
        )

        evento.save()

        messages.add_message(request, constants.SUCCESS,
                             _("Evento cadastrado com sucesso"))
        return redirect(reverse("novo_evento"))


@login_required  # type: ignore
def gerenciar_evento(request):
    if request.method == "GET":
        _nome = request.GET.get('nome')
        eventos = Evento.objects.filter(criador=request.user)

        if _nome:
            eventos = eventos.filter(nome__contains=_nome)
        # TODO: realizar outros filtros (Datas, período de datas, descrição)

        return render(request, "gerenciar_evento.html", {'eventos': eventos})


@login_required # type: ignore
def inscrever_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    print(evento.data_inicio)
    if request.method == "GET":
        return render(request, "inscrever_evento.html", {"evento": evento})
    elif request.method == "POST":
        # TODO: validar se o usuário já é participante
        
        evento.participantes.add(request.user)
        evento.save()
        messages.add_message(request, constants.SUCCESS, _("Inscrição realizada com sucesso!"))
        return redirect(reverse('inscrever_evento', kwargs={'id': id}))

def participantes_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    if request.method == "GET":
        participantes = evento.participantes.all()[::3]
        return render(request, "participantes_evento.html", {"participantes": participantes})
