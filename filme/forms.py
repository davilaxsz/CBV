from django import forms
from .models import Filme

class FilmeForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = ['titulo', 'diretor', 'genero', 'ano', 'avaliacao']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'diretor': forms.TextInput(attrs={'class': 'form-control'}),
            'genero': forms.TextInput(attrs={'class': 'form-control'}),
            'ano': forms.NumberInput(attrs={'class': 'form-control'}),
            'avaliacao': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'min': '0', 'max': '10'}),
        }
