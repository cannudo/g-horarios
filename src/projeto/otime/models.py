from django.db import models

# Create your models here.

###############################--Salas--#####################################

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
    def __str__(self):
        return "Sala de aula #%d: %s" % (int(self.id), self.nome)

    class Meta:
        verbose_name_plural = 'Salas de aulas'

##############################--Disciplinas--##################################

class Disciplina(models.Model):
    nome = models.CharField(max_length = 25)
    codigo = models.CharField(max_length = 25)
    carga_horaria_total = models.IntegerField()
    def __str__(self):
        return "Disciplina #%d: %s" % (int(self.id), self.nome)

    class Meta:
        verbose_name_plural = 'disciplinas'

##############################--Professores--################################

class Professor(models.Model):
    nome = models.CharField(max_length = 45)
    telefone = models.CharField(max_length = 15)
    email = models.CharField(max_length = 90)
    matricula = models.CharField(max_length = 15)
    def __str__(self):
        return "Professor #%d: %s" % (int(self.id), self.nome)

    class Meta:
        verbose_name_plural = 'professores'

###############################--Turma--###############################

class Turma(models.Model):
    opcoes = (
        ("Matutino", "Matutino"),
        ("Vespertino", "Vespertino"),
    )
    turno = models.CharField(max_length = 15, choices = opcoes)
    nome = models.CharField(max_length = 50)
    def __str__(self):
        return "Turma #%d: %s" % (int(self.id), self.nome)
        
    class Meta:
        verbose_name_plural = 'turmas'

##############################--Slot de Horários--################################

class SlotDeHorario(models.Model):
    posicao = models.IntegerField(unique = True)
    sala_de_aula = models.ForeignKey(SalaDeAula, on_delete = models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete = models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete = models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete = models.CASCADE)
    def __str__(self):
        return "Slot #%d" % int(self.posicao)

    class Meta:
        verbose_name_plural = 'Slots de horarios'
