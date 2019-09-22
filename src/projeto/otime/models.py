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
    numero = models.IntegerField(unique = True)

class Disciplina(models.Model):
    nome = models.CharField(max_length = 25)
    codigo = models.CharField(max_length = 25)
    carga_horaria_total = models.IntegerField()

class Professor(models.Models):
    nome = models.CharField(max_length = 45)
