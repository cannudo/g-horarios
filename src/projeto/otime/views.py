from django.shortcuts import render
from .models import SalaDeAula, Disciplina

# Create your views here.
def index(request):
    lista_de_salas = SalaDeAula.objects.all()
    lista_de_disciplinas = Disciplinas.objects.all()
    contexto = {
        "lista_de_salas": lista_de_salas,
        "lista_de_disciplinas": lista_de_disciplinas
    }
    return render(request, "otime/index.html", contexto)
