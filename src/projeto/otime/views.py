from django.shortcuts import render
from .models import SalaDeAula, Disciplina, Professor

# Create your views here.
def index(request):
    lista_de_salas = SalaDeAula.objects.all()
    lista_de_disciplinas = Disciplina.objects.all()
    lista_de_professores = Professor.objects.all()
    contexto = {
        "lista_de_salas": lista_de_salas,
        "lista_de_disciplinas": lista_de_disciplinas,
        "lista_de_professores": lista_de_professores
    }
    return render(request, "otime/index.html", contexto)

def reservarHorario(request):
    lista_de_salas = SalaDeAula.objects.all()
    lista_de_disciplinas = Disciplina.objects.all()
    lista_de_professores = Professor.objects.all()
    contexto = {
        "lista_de_salas": lista_de_salas,
        "lista_de_disciplinas": lista_de_disciplinas,
        "lista_de_professores": lista_de_professores
    }
    return render(request, "otime/reservar-horario.html", contexto)
