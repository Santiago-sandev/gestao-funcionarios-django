# 🏢 Sistema de Gestão de Funcionários e Projetos

Sistema completo de gestão de funcionários e projetos desenvolvido com **Django** e **MySQL**, para aprendizado.

## 🚀 Tecnologias Utilizadas

- **Backend:** Django 5.2.3
- **Banco de Dados:** MySQL 8.0
- **Frontend:** Bootstrap 5 + Font Awesome
- **Controle de Versão:** Git

## ✨ Funcionalidades

### 👥 Gestão de Funcionários
- ✅ Cadastro completo (nome, cargo, email, telefone)
- ✅ Controle de status (ativo/inativo)
- ✅ Data de contratação
- ✅ Histórico de criação e atualização

### 🎛️ Gestão de Projetos
- ✅ Cadastro de projetos com descrição detalhada
- ✅ Controle de status (em andamento, concluído, parado)
- ✅ Datas de início e término previsto
- ✅ Relacionamento muitos-para-muitos com funcionários

### 🎛️ Painel Administrativo
- ✅ Interface completa do Django Admin
- ✅ Filtros e pesquisas avançadas
- ✅ Dashboard com estatísticas
- ✅ Gerenciamento de relacionamentos

### 🌐 Interface Web
- ✅ Dashboard responsivo com estatísticas
- ✅ Listagem de funcionários e projetos
- ✅ Páginas de detalhes individuais
- ✅ Design moderno com Bootstrap

## 🛠️ Instalação e Configuração

### Pré-requisitos
- Python 3.8+
- MySQL 8.0+
- Git

### Passos para instalação

1. **Clone o repositório**
   ```bash
   git clone https://github.com/SEU_USUARIO/gestao-funcionarios-django.git
   cd gestao-funcionarios-django
   ```

2. **Crie e ative o ambiente virtual**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure o banco de dados**
   - Crie um banco MySQL chamado `gestao_funcionarios_db`
   - Configure as credenciais em `gestao_funcionarios/settings.py`

5. **Execute as migrações**
   ```bash
   python manage.py migrate
   ```

6. **Crie um superusuário**
   ```bash
   python manage.py createsuperuser
   ```

7. **Execute o servidor**
   ```bash
   python manage.py runserver
   ```

## 📱 Como usar

1. **Acesse o sistema:** `http://127.0.0.1:8000/`
2. **Painel admin:** `http://127.0.0.1:8000/admin/`
3. **Adicione funcionários e projetos pelo admin**
4. **Visualize os dados nas páginas web**

## 🗂️ Estrutura do Projeto

gestao-funcionarios-django/
├── gestao_funcionarios/ # Configurações do projeto
├── funcionarios/ # Aplicação principal
│ ├── models.py # Modelos de dados
│ ├── views.py # Lógica das páginas
│ ├── admin.py # Configuração do admin
│ └── templates/ # Templates HTML
├── manage.py # Comando principal do Django
└── requirements.txt # Dependências do projeto

## 🎯 Recursos Técnicos

- **ORM Django** com relacionamentos N:N
- **Django Admin** customizado
- **Templates** com herança
- **URLs** organizadas
- **Migrações** do banco
- **API** JSON para dashboard

## 👨‍💻 Autor

[Guilherme Santiago - san] - [guiking08@gmail.com]

---

**Projeto desenvolvido para portfólio e aprendizado de Django.**

