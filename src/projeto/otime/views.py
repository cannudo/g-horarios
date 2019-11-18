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

def reservarHorario(request, id):
    if request.method == "POST":
        turma = get_object_or_404(Turma, pk = id)
        sala_de_aula = get_object_or_404(SalaDeAula, pk = request.POST["sala_de_aula"])
        disciplina = get_object_or_404(Disciplina, pk = request.POST["disciplina"])
        professor = get_object_or_404(Professor, pk = request.POST["professor"])
        for horario in request.POST.getlist("horarios"):
            slot_de_horario = SlotDeHorario(turma = turma, posicao = horario, sala_de_aula = sala_de_aula, disciplina = disciplina, professor = professor)

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
    form = FormSala(request.POST or None)
    if form.is_valid():
        form.save()

    lista_de_salas = SalaDeAula.objects.all()
    return render(request,'otime/salas.html',{'lista_de_salas':lista_de_salas, 'form': form})

def disciplinas(request):
    form = FormDisciplina(request.POST or None)

    if form.is_valid():
        form.save()

    lista_de_disciplinas = Disciplina.objects.all()
    return render(request,'otime/disciplinas.html',{'lista_de_disciplinas':lista_de_disciplinas, 'form': form})

def professores(request):
    form =  FormProfessor(request.POST or None)
    if form.is_valid():
        form.save()

    lista_de_professores = Professor.objects.all()
    return render(request,'otime/professores.html',{'lista_de_professores':lista_de_professores, 'form':form})

##View para exibir as turmas cadastradas e
##selecionar a que irá ser definida os horarios na view de reserva de horario.
def seletor_turmas(request):
    lista_de_turmas = Turma.objects.all()
    return render(request,'otime/seletor_turmas.html',{'lista_de_turmas':lista_de_turmas})

def turmas(request):
    form =  FormTurma(request.POST or None)
    if form.is_valid():
        form.save()

    lista_de_turmas = Turma.objects.all()
    return render(request,'otime/turmas.html',{'lista_de_turmas':lista_de_turmas, 'form':form})

def atualizar_turma(request, id):
    turma = Turma.objects.get(id=id)
    form =  FormTurma(request.POST or None, instance=turma)

    if form.is_valid():
        form.save()
        return redirect('turmas')

    if request.method == 'POST':
        turma.delete()
        return redirect('turmas')

    return render(request, 'otime/modais/editar-turma.html', {'form': form, 'turma': turma})

def atualizar_professor(request, id):
    professor = Professor.objects.get(id=id)
    form =  FormProfessor(request.POST or None, instance=professor)

    if form.is_valid():
        form.save()
        return redirect('professores')

    if request.method == 'POST':
        professor.delete()
        return redirect('professores')

    return render(request, 'otime/modais/editar-prof.html', {'form': form, 'professor': professor})

def atualizar_sala(request, id):
    sala = SalaDeAula.objects.get(id=id)
    form =  FormSala(request.POST or None, instance=sala)

    if form.is_valid():
        form.save()
        return redirect('salas')

    if request.method == 'POST':
        sala.delete()
        return redirect('salas')

    return render(request, 'otime/modais/editar-sala.html', {'form': form, 'sala': sala})

def atualizar_disciplina(request, id):
    disciplina = Disciplina.objects.get(id=id)
    form =  FormDisciplina(request.POST or None, instance=disciplina)

    if form.is_valid():
        form.save()
        return redirect('disciplinas')

    if request.method == 'POST':
        disciplina.delete()
        return redirect('disciplinas')

    return render(request, 'otime/modais/editar-disc.html', {'form': form, 'disciplina': disciplina})

def modelo(request):
    lista_de_professores = Professor.objects.all()

    if request.method == 'POST':
        metodo = request.POST['metodo']
        if metodo == "criar":
            professor = get_object_or_404(Professor, pk = request.POST["id"])
            professor.save()
        elif metodo == "atualizar":
            # Atualizará um objeto Professor
            pass
        elif metodo == "deletar":
            # Deletará um objeto Professor
            pass

    return render(request, 'otime/professores.html', {'lista_de_professores': lista_de_professores})
