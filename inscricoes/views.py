from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Inscricao
from eventos.models import Evento

@login_required
def inscrever(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    
    if Inscricao.objects.filter(usuario=request.user, evento=evento).exists():
        messages.warning(request, "Você já está inscrito neste evento.")
        return redirect('eventos:lista')
    
    if evento.vagas <= 0:
        messages.error(request, "Não é possível se inscrever, pois não há vagas disponíveis.")
        return redirect('eventos:lista')
    
    Inscricao.objects.get_or_create(usuario=request.user, evento=evento)
    evento.vagas -= 1
    evento.save()
    messages.success(request, "Inscrição realizada com sucesso!")
    return redirect('inscricoes:minhas_inscricoes')

@login_required
def minhas_inscricoes(request):
    inscricoes = Inscricao.objects.filter(usuario=request.user).select_related('evento')
    return render(request, 'inscricoes/minhas.html', {'inscricoes': inscricoes})
