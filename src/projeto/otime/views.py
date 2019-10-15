from django.shortcuts import render, get_object_or_404,redirect
from .models import *
from .forms import *

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
    if request.method == "POST":
        requisicao_post = request.POST
        sala_de_aula = get_object_or_404(SalaDeAula, pk = requisicao_post["sala_de_aula"])
        disciplina = get_object_or_404(Disciplina, pk = requisicao_post["disciplina"])
        professor = get_object_or_404(Professor, pk = requisicao_post["professor"])
        slot_de_horario = SlotDeHorario(posicao = requisicao_post["posicao"], sala_de_aula = sala_de_aula, disciplina = disciplina, professor = professor)
        slot_de_horario.save()

    slots_de_horario = SlotDeHorario.objects.all()
    lista_de_salas = SalaDeAula.objects.all()
    lista_de_disciplinas = Disciplina.objects.all()
    lista_de_professores = Professor.objects.all()
    horarios = "07h00-07h45 07h45-08h30 09h00-09h45 09h45-10h30 10h30-11h15 11h15-12h00 13h00-13h45 13h45-14h30 14h30-15h15 15h15-16h00 16h30-17h15 15h15-18h00 19h00-19h45 19h45-20h30 20h40-21h25 21h25-22h10"
    contexto = {
        "slots_de_horario": slots_de_horario,
        "lista_de_salas": lista_de_salas,
        "lista_de_disciplinas": lista_de_disciplinas,
        "lista_de_professores": lista_de_professores,
        "horarios": horarios,
    }
    return render(request, "otime/reservar-horario.html", contexto)


def salas(request):
    lista_de_salas = SalaDeAula.objects.all()
    return render(request,'otime/salas.html',{'lista_de_salas':lista_de_salas})

def professores(request):
    lista_de_professores = Professor.objects.all()
    return render(request,'otime/professores.html',{'lista_de_professores':lista_de_professores})

def disciplinas(request):
    lista_de_disciplinas = Disciplina.objects.all()
    return render(request,'otime/disciplinas.html',{'lista_de_disciplinas':lista_de_disciplinas})

def criar_professor(request):
    form = FormProfessor(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('professores')

    return render(request, 'otime/professor-form.html', {'form': form})

def criar_disciplina(request):
    form = FormDisciplina(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('disciplinas')

    return render(request, 'otime/disciplina-form.html', {'form': form})

def atualizar_professor(request, id):
    professor = Professor.objects.get(id=id)
    form =  FormProfessor(request.POST or None, instance=professor)

    if form.is_valid():
        form.save()
        return redirect('lista_de_professores')

    return render(request, 'otime/professor-form.html', {'form': form, 'professor': professor})

def atualizar_disciplina(request, id):
    disciplina = Disciplina.objects.get(id=id)
    form =  FormDisciplina(request.POST or None, instance=disciplina)

    if form.is_valid():
        form.save()
        return redirect('lista_de_disciplinas')

    return render(request, 'otime/disciplina-form.html', {'form': form, 'disciplina': disciplina})

def deletar_professor(request, id):
    professor = Professor.objects.get(id=id)

    if request.method == 'POST':
        professor.delete()
        return redirect('lista_de_professores')

    return render(request, 'otime/prof-delete-confirm.html', {'professor': professor})

def deletar_disciplina(request, id):
    disciplina = Disciplina.objects.get(id=id)

    if request.method == 'POST':
        disciplina.delete()
        return redirect('lista_de_disciplinas')

    return render(request, 'otime/disc-delete-confirm.html', {'disciplina': disciplina})

def modelo(request):
    lista_de_professores = Professor.objects.all()

    if request.method == 'POST':
        pass

    return render(request, 'otime/professores.html', {'lista_de_professores': lista_de_professores})
