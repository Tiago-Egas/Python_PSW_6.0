from django.shortcuts import redirect, render
from django.utils.translation import gettext as _
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required # type: ignore
def novo_evento(request):
    if request.method == "GET":
        return render(request, "novo_evento.html")