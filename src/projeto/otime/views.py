from django.shortcuts import render
from django.http import HttpResponse
from .models import SalaDeAula

# Create your views here.
def index(request):
    lista_de_salas = SalaDeAula.objects.all()
    contexto = {
        "lista_de_salas": lista_de_salas
    }
    return HttpResponse("Olá, mundo! Isto é temporário.")
