from django.db import models
from django.conf import settings
from eventos.models import Evento

class Certificado(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    data_emissao = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'evento')

    def __str__(self):
        return f'Certificado {self.usuario} - {self.evento}'
