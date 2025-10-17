from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Evento
from .forms import EventoForm
from inscricoes.models import Inscricao
from django.contrib.auth.decorators import login_required

def lista_eventos(request):
    eventos = Evento.objects.all().order_by('data_inicio')
    return render(request, 'eventos/lista.html', {'eventos': eventos})

def detalhe_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    inscritos = Inscricao.objects.filter(evento=evento).select_related('usuario')
    return render(request, 'eventos/detalhe.html', {'evento': evento, 'inscritos': inscritos})

@login_required
def criar_evento(request):
    if request.user.perfil != 'organizador':
        messages.error(request, "Apenas organizadores podem criar eventos.")
        return redirect('eventos:lista')

    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            evento = form.save(commit=False)
            evento.organizador = request.user
            evento.save()
            messages.success(request, "Evento criado com sucesso!")
            return redirect('eventos:lista')
    else:
        form = EventoForm()
    return render(request, 'eventos/criar.html', {'form': form})
