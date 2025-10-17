import os
import django
from datetime import datetime, timedelta


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sgea.settings')
django.setup()

from django.contrib.auth import get_user_model
from eventos.models import Evento

User = get_user_model()

def popular_banco():

    organizador, created = User.objects.get_or_create(
        username='organizador',
        defaults={
            'email': 'organizador@sgea.com',
            'first_name': 'Organizador',
            'last_name': 'Padrão',
            'is_staff': True,
            'is_superuser': False,
        }
    )

    if created:
        organizador.set_password('Org123456')
        organizador.save()


    Evento.objects.all().delete()


    eventos = [
        {
            'titulo': 'Seminário de Inteligência Artificial',
            'tipo': 'seminario',
            'data_inicio': datetime(2025, 10, 20, 19, 0),
            'data_fim': datetime(2025, 10, 20, 22, 0),
            'horario': '19:00 - 22:00',
            'local': 'Auditório Central',
            'vagas': 100
        },
        {
            'titulo': 'Palestra sobre Segurança da Informação',
            'tipo': 'palestra',
            'data_inicio': datetime(2025, 10, 22, 18, 30),
            'data_fim': datetime(2025, 10, 22, 20, 0),
            'horario': '18:30 - 20:00',
            'local': 'Sala 101 - Bloco A',
            'vagas': 80
        },
        {
            'titulo': 'Minicurso de Python para Iniciantes',
            'tipo': 'minicurso',
            'data_inicio': datetime(2025, 10, 24, 14, 0),
            'data_fim': datetime(2025, 10, 24, 18, 0),
            'horario': '14:00 - 18:00',
            'local': 'Laboratório de Informática 2',
            'vagas': 25
        },
        {
            'titulo': 'Semana Acadêmica de Tecnologia',
            'tipo': 'semana',
            'data_inicio': datetime(2025, 11, 3, 9, 0),
            'data_fim': datetime(2025, 11, 7, 18, 0),
            'horario': '09:00 - 18:00',
            'local': 'Campus Principal',
            'vagas': 300
        }
    ]

    for e in eventos:
        Evento.objects.create(
            organizador=organizador,
            **e
        )

    print("Banco de dados populado com sucesso com todos os eventos!")

if __name__ == "__main__":
    popular_banco()
