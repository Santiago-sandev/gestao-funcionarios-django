from django.urls import path
from . import views

app_name = 'funcionarios'

urlpatterns = [
    path('', views.home, name='home'),
    path('funcionarios/', views.lista_funcionarios, name='lista_funcionarios'),
    path('projetos/', views.lista_projetos, name='lista_projetos'),
    path('funcionario/<int:funcionario_id>/', views.detalhe_funcionario, name='detalhe_funcionario'),
    path('projeto/<int:projeto_id>/', views.detalhe_projeto, name='detalhe_projeto'),
    path('api/dashboard/', views.api_dashboard, name='api_dashboard'),
]