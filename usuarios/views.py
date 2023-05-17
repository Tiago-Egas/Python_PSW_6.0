from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.translation import gettext as _
from django.contrib import messages, auth
from django.contrib.messages import constants

# Create your views here.


def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        confirm_password = request.POST.get("confirm_password")

        if not password == confirm_password:
            messages.add_message(request, constants.ERROR,
                                 _("As senhas não coincidem!"))
            return redirect(reverse('cadastro'))

        user = User.objects.filter(username=username)

        # TODO: Validar força da senha

        if user.exists():
            messages.add_message(request, constants.ERROR,
                                 _("Usuário já cadastrado!"))
            return redirect(reverse("cadastro"))

        user = User.objects.create_user(
            username=username, password=password, email=email)
        messages.add_message(request, constants.SUCCESS,
                             _("Usuário salvo com sucesso!"))

        return redirect(reverse('login'))


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = auth.authenticate(username=username, password=senha)

        if not user:
            messages.add_message(request, constants.ERROR,
                                 _("Username ou senha inválidos"))
            return redirect(reverse('login'))

        auth.login(request, user)
        return redirect('/eventos/novo_evento/')
