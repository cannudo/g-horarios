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
