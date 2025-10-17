from django.urls import path
from . import views

app_name = 'inscricoes'
urlpatterns = [
    path('inscrever/<int:evento_id>/', views.inscrever, name='inscrever'),
    path('minhas/', views.minhas_inscricoes, name='minhas_inscricoes'),
]
