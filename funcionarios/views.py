from django.shortcuts import render
from django.http import JsonResponse
from .models import Funcionario, Projeto

def home(request):
    """Página inicial com dashboard básico"""
    context = {
        'total_funcionarios': Funcionario.objects.count(),
        'total_projetos': Projeto.objects.count(),
        'funcionarios_ativos': Funcionario.objects.filter(status='ativo').count(),
        'projetos_em_andamento': Projeto.objects.filter(status='em_andamento').count(),
        'ultimos_funcionarios': Funcionario.objects.order_by('-data_criacao')[:5],
        'ultimos_projetos': Projeto.objects.order_by('-data_criacao')[:5],
    }
    return render(request, 'funcionarios/home.html', context)

def lista_funcionarios(request):
    """Lista todos os funcionários"""
    funcionarios = Funcionario.objects.all().order_by('nome')
    context = {
        'funcionarios': funcionarios,
        'total': funcionarios.count(),
    }
    return render(request, 'funcionarios/lista_funcionarios.html', context)

def lista_projetos(request):
    """Lista todos os projetos"""
    projetos = Projeto.objects.all().order_by('nome')
    context = {
        'projetos': projetos,
        'total': projetos.count(),
    }
    return render(request, 'funcionarios/lista_projetos.html', context)

def detalhe_funcionario(request, funcionario_id):
    """Mostra detalhes de um funcionário específico"""
    try:
        funcionario = Funcionario.objects.get(id=funcionario_id)
        projetos = funcionario.projeto_set.all()
        context = {
            'funcionario': funcionario,
            'projetos': projetos,
        }
        return render(request, 'funcionarios/detalhe_funcionario.html', context)
    except Funcionario.DoesNotExist:
        return render(request, 'funcionarios/erro.html', {'mensagem': 'Funcionário não encontrado'})

def detalhe_projeto(request, projeto_id):
    """Mostra detalhes de um projeto específico"""
    try:
        projeto = Projeto.objects.get(id=projeto_id)
        context = {
            'projeto': projeto,
            'funcionarios': projeto.funcionarios.all(),
        }
        return render(request, 'funcionarios/detalhe_projeto.html', context)
    except Projeto.DoesNotExist:
        return render(request, 'funcionarios/erro.html', {'mensagem': 'Projeto não encontrado'})

def api_dashboard(request):
    """API para dados do dashboard (JSON)"""
    data = {
        'total_funcionarios': Funcionario.objects.count(),
        'total_projetos': Projeto.objects.count(),
        'funcionarios_ativos': Funcionario.objects.filter(status='ativo').count(),
        'projetos_em_andamento': Projeto.objects.filter(status='em_andamento').count(),
    }
    return JsonResponse(data)