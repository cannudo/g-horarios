from django.test import TestCase
from django.test import TestCase
from otime.models import *
# Create your tests here.

salas = (
    ("Laboratório 01", "Laboratório", 1),
    ("Laboratório 02", "Laboratório", 2),
    ("Laboratório 03", "Laboratório", 3),
    ("Sala de Reuniões", "Sala regular", 25),
)

disciplinas = (
    ("IHC", "25785", 60),
    ("Reunião", "402", 0),
    ("Web Design", "28635", 60),
)

professores = (
    ("Silvia Matos", "5845852", "silvia.matos", "452425400"),
    ("Fellipe Aleixo", "584355852", "fellipe.aleixo", "548754"),
    ("Hugo Melo", "5720852", "hugo.melo", "452425400"),
)

for i in range(len(salas)):
    sala = SalaDeAula(nome = salas[i][0], tipo = salas[i][1], numero = salas[i][2])
    sala.save()

for i in range(len(disciplinas)):
    disciplina = Disciplina(nome = disciplinas[i][0], codigo = disciplinas[i][1], carga_horaria_total = disciplinas[i][2])
    disciplina.save()

for i in range(len(professores)):
    professor = Professor(nome = professores[i][0], telefone = professores[i][1], email = professores[i][2], matricula = professores[i][3])
    professor.save()
