from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from .models import Certificado
from inscricoes.models import Inscricao
from eventos.models import Evento
from django.contrib.auth import get_user_model

User = get_user_model()

@login_required
def emitir_certificado(request, evento_id, usuario_id=None):
    evento = get_object_or_404(Evento, id=evento_id)
    
    if request.user != evento.organizador:
        messages.error(request, "Apenas o organizador deste evento pode emitir certificados.")
        return redirect('eventos:lista')

    if usuario_id is None:
        user = request.user
    else:
        user = get_object_or_404(User, id=usuario_id)

    inscricao_exists = Inscricao.objects.filter(usuario=user, evento=evento).exists()
    if not inscricao_exists:
        messages.error(request, "O usuário selecionado não está inscrito neste evento.")
        return redirect('eventos:lista')

    certificado, _ = Certificado.objects.get_or_create(usuario=user, evento=evento)
    messages.success(request, "Certificado emitido com sucesso!")
    return render(request, 'certificados/detalhe.html', {'certificado': certificado, 'evento': evento})

@login_required
def meus_certificados(request):
    certificados = Certificado.objects.filter(usuario=request.user)
    return render(request, 'certificados/meus_certificados.html', {'certificados': certificados})