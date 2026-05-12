# Lab 1 - Django Backend (Task Manager)

**Disciplina:** [Backend Frameworks]  
**Turma:** [B]  
**Aluno:** [Jorge Augusto Melém da Silva Lima]
Matrícula: 26159658
---

##  Objetivo do Laboratório

Desenvolver uma aplicação web utilizando o framework **Django** para gerenciar tarefas (CRUD completo), incluindo:

- Criação de modelo `Task`
- Interface administrativa
- CRUD completo via formulários (listar, criar, editar e excluir tarefas)
- Templates HTML básicos
- Configuração de rotas e views

---

##  Tecnologias Utilizadas

- **Python**
- **Django** (Framework Web)
- **SQLite** (banco de dados padrão)
- **HTML5 + CSS** (Templates)
- **Git + GitHub** (Versionamento)

---

##  Como Executar o Projeto

### Pré-requisitos
- Python 3.8+ instalado
- Git instalado (opcional)

### Passo a passo

1. **Clone o repositório**
   ```bash
   git clone https://github.com/ProgJL/Lab-Django.git
   cd Lab-Django

2.Aplique as migrações
python manage.py makemigrations
python manage.py migrate


3.Crie um superusuário (admin)
python manage.py createsuperuser


4. Execute o servidor
python manage.py runserver

5. Acesse a aplicação
Aplicação principal: http://127.0.0.1:8000/
Painel Administrativo: http://127.0.0.1:8000/admin/