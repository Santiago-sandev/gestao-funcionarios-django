from django.db import models

class Funcionario(models.Model):
    # Campos básicos
    nome = models.CharField(max_length=100, verbose_name="Nome")
    cargo = models.CharField(max_length=100, verbose_name="Cargo")
    email = models.EmailField(verbose_name="E-mail")
    telefone = models.CharField(max_length=20, verbose_name="Telefone")

    # Datas
    data_contratacao = models.DateField(verbose_name="Data de Contratação")

    # Status
    STATUS_CHOICES = [
        ('ativo', 'Ativo'),
        ('inativo', 'Inativo'),
    ]
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='ativo',
        verbose_name="Status"
    )

    # Timestamps automáticos
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    data_atualizacao = models.DateTimeField(auto_now=True, verbose_name="Última Atualização")
    
    def __str__(self):
        return self.nome
        
    class Meta:
        verbose_name = "Funcionário"
        verbose_name_plural = "Funcionários"

class Projeto(models.Model):
    # Campos Básicos
    nome = models.CharField(max_length=200, verbose_name="Nome do Projeto")
    descricao = models.TextField(verbose_name="Descrição")

    # Datas
    data_inicio = models.DateField(verbose_name="Data de Início")
    data_termino_previsto = models.DateField(verbose_name="Data Prevista de Término")

    # Status
    STATUS_CHOICES = [
        ('em_andamento', 'Em Andamento'),
        ('concluido', 'Concluído'),
        ('parado', 'Parado'),
    ]
    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default='em_andamento',
        verbose_name="Status"
    )

    # Relacionamento muitos-para-muitos com Funcionário
    funcionarios = models.ManyToManyField(
        Funcionario,
        verbose_name="Funcionários",
        blank=True
    )

    # Timestamps automáticos
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    data_atualizacao = models.DateTimeField(auto_now=True, verbose_name="Última Atualização")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"
# Create your models here.
