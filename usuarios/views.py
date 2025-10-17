from .forms import LoginForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UsuarioCadastroForm
from django.contrib import messages

def cadastro(request):
    if request.method == 'POST':
        form = UsuarioCadastroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cadastro realizado com sucesso!")
            return redirect('usuarios:login')
        else:
            messages.error(request, "Corrija os erros abaixo.")
    else:
        form = UsuarioCadastroForm()
    return render(request, 'usuarios/cadastro.html', {'form': form})

def login_usuario(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login realizado com sucesso!")
                return redirect('pagina_inicial')
            else:
                messages.error(request, "Usuário ou senha inválidos.")
    else:
        form = LoginForm()
    return render(request, 'usuarios/login.html', {'form' : form})


def logout_usuario(request):
    logout(request)
    return render(request, 'usuarios/logout.html')
