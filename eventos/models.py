from django.db import models
from django.conf import settings

class Evento(models.Model):
    TIPOS = [
        ('seminario', 'Seminário'),
        ('palestra', 'Palestra'),
        ('minicurso', 'Minicurso'),
        ('semana', 'Semana Acadêmica'),
    ]
    titulo = models.CharField(max_length=200)
    tipo = models.CharField(max_length=50, choices=TIPOS)
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    horario = models.CharField(max_length=100)
    local = models.CharField(max_length=200)
    vagas = models.PositiveIntegerField(default=0)
    organizador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
