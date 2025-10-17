from django.urls import path
from . import views

app_name = 'eventos'
urlpatterns = [
    path('', views.lista_eventos, name='lista'),
    path('criar/', views.criar_evento, name='criar'),
    path('<int:id>/', views.detalhe_evento, name='detalhe'),
]
