from django import forms
from .models import Professor


class FormProfessor(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['nome', 'telefone', 'email', 'matricula']



