from django.urls import path
from . import views

app_name = 'certificados'
urlpatterns = [
    path('emitir/<int:evento_id>/<int:usuario_id>/', views.emitir_certificado, name='emitir'),
    path('meus/', views.meus_certificados, name='meus_certificados'),
]
