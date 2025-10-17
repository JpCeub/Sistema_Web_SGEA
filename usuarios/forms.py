from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class UsuarioCadastroForm(UserCreationForm):
    nome = forms.CharField(label='Nome completo', required=True)
    telefone = forms.CharField(label='Telefone', required=True)
    perfil = forms.ChoiceField(choices=Usuario.PERFIS, label='Perfil', required=True)
    instituicao = forms.CharField(label='Instituição', required=False)
    email = forms.EmailField(label='E-mail', required=True)

    class Meta:
        model = Usuario
        fields = [
            'nome',
            'telefone',
            'perfil',
            'instituicao',
            'username',   
            'email',
            'password1',  
            'password2',  
        ]
        labels = {
            'username': 'Usuário de login',
            'password1': 'Senha',
            'password2': 'Confirmar senha',
        }

    def clean(self):
        cleaned_data = super().clean()
        perfil = cleaned_data.get('perfil')
        instituicao = cleaned_data.get('instituicao')
        if perfil in ['aluno', 'professor'] and not instituicao:
            self.add_error('instituicao', 'A instituição é obrigatória para alunos e professores.')
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['nome']
        user.telefone = self.cleaned_data['telefone']
        user.perfil = self.cleaned_data['perfil']
        user.instituicao = self.cleaned_data.get('instituicao', '')
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
class LoginForm(forms.Form):
    username = forms.CharField(label='Usuário de login', max_length=150)
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)
