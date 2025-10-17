from django.urls import path
from . import views

app_name = 'usuarios'
urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login_usuario, name='login'),
    path('logout/', views.logout_usuario, name='logout'),
]
