from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='pagina_inicial'),
    path('usuarios/', include('usuarios.urls')),
    path('eventos/', include('eventos.urls')),
    path('inscricoes/', include('inscricoes.urls')),
    path('certificados/', include('certificados.urls')),
]
