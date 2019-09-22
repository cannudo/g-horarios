from django.db import models

# Create your models here.
class SalaDeAula(models.Model):
    nome = models.CharField(max_length = 40)
    tipos = (
        ("Sala regular", "Sala regular"),
        ("Laboratório", "Laboratório"),
        ("Audiovisual", "Audiovisual"),
        ("Auditório", "Auditório"),
        ("Miniauditório", "Miniauditório"),
    )
    tipo = models.CharField(max_length = 15, choices = tipos)
    numero = models.IntegerField()

class Disciplina(models.Model):
    nome = models.CharField(max_length = 25)
    codigo = models.CharField(max_length = 25)
    carga_horaria_total = models.IntegerField()

class Professor(models.Model):
    nome = models.CharField(max_length = 45)
    telefone = models.CharField(max_length = 15)
    email = models.CharField(max_length = 90)
    matricula = models.CharField(max_length = 15)

class SlotDeHorario(models.Model):
    posicao = models.IntegerField(unique = True)
    sala_de_aula = models.ForeignKey(SalaDeAula, on_delete = models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete = models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete = models.CASCADE)
