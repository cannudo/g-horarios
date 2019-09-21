from django.db import models

# Create your models here.
class SalaDeAula(models.Model):
    nome = models.CharField(max_length = 40)
