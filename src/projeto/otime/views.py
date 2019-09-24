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
    texto = "A requisição foi %s" % request.method

    lista_de_salas = SalaDeAula.objects.all()
    lista_de_disciplinas = Disciplina.objects.all()
    lista_de_professores = Professor.objects.all()
    horarios = "07h00-07h45 07h45-08h30 09h00-09h45 09h45-10h30 10h30-11h15 11h15-12h00 13h00-13h45 13h45-14h30 14h30-15h15 15h15-16h00 16h30-17h15 15h15-18h00 19h00-19h45 19h45-20h30 20h40-21h25 21h25-22h10"
    contexto = {
        "lista_de_salas": lista_de_salas,
        "lista_de_disciplinas": lista_de_disciplinas,
        "lista_de_professores": lista_de_professores,
        "horarios": horarios,
        "texto": texto,
    }
    return render(request, "otime/reservar-horario.html", contexto)
