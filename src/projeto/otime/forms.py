from django import forms
from .models import Professor
from .models import Disciplina
from .models import SalaDeAula

class FormProfessor(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['nome', 'telefone', 'email', 'matricula']

class FormDisciplina(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = ['nome', 'codigo', 'carga_horaria_total']

class FormSala(forms.ModelForm):
    class Meta:
        model = SalaDeAula
        fields = ['nome', 'tipo', 'numero']
