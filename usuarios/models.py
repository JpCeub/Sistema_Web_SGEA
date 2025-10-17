from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    PERFIS = [
        ('aluno', 'Aluno'),
        ('professor', 'Professor'),
        ('organizador', 'Organizador'),
    ]
    telefone = models.CharField(max_length=20, blank=False)
    instituicao = models.CharField(max_length=150, blank=True)
    perfil = models.CharField(max_length=20, choices=PERFIS, default='aluno')

    def __str__(self):
        return self.get_full_name() or self.username
