from django.contrib import admin
from .models import Funcionario, Projeto

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cargo', 'email', 'status', 'data_contratacao']
    list_filter = ['status', 'cargo', 'data_contratacao']
    search_fields = ['nome', 'email', 'cargo']
    list_per_page = 20

    fieldsets = (
        ('Informações Básicas', {
            'fields': ('nome', 'cargo', 'email', 'telefone')
        }),
        ('Status e Datas', {
            'fields': ('status', 'data_contratacao')
        }),
    )

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'status', 'data_inicio', 'data_termino_previsto', 'get_funcionarios_count']
    list_filter = ['status', 'data_inicio']
    search_fields = ['nome', 'descricao']
    list_per_page = 20

    fieldsets = (
        ('Informações do Projeto', {
            'fields': ('nome', 'descricao')
        }),
        ('Datas e Status', {
            'fields': ('data_inicio', 'data_termino_previsto', 'status')
        }),
        ('Funcionários', {
            'fields': ('funcionarios',)
        }),
    )

    def get_funcionarios_count(self, obj):
        return obj.funcionarios.count()
    get_funcionarios_count.short_description = 'Funcionários'