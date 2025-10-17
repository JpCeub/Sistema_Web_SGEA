from django import forms
from .models import Evento

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['titulo', 'tipo', 'data_inicio', 'data_fim', 'horario', 'local', 'vagas']
        widgets = {
            'horario': forms.TimeInput(attrs={'placeholder': 'hh:mm'}),
            'data_inicio': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'data_fim': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        