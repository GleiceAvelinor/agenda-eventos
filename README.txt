## Projeto criando por Gleice Avelino
---

# 📅 Agenda de Eventos

Uma aplicação web desenvolvida em **Django 6.0+** para gerenciamento e agendamento de compromissos e eventos pessoais. O projeto conta com autenticação de usuários, associação de eventos por perfil e painel administrativo integrado.

---

## 🚀 Funcionalidades

- Gerenciamento de Eventos: criação, edição, visualização e remoção de compromissos.
- Autenticação de Usuários: cadastro e login seguro, garantindo que cada usuário visualize apenas seus próprios eventos.
- Painel Administrativo: interface do Django Admin habilitada para gestão completa do sistema.

---

## 🛠️ Tecnologias Utilizadas

- Python 3.14+
- Django 6.0+
- uv ou pip
- SQLite3 (ambiente de desenvolvimento)

---

## 📂 Estrutura do Projeto

```text
agenda/
├── core/                  # App principal (Eventos e Regras de Negócio)
├── agenda/                # Configurações globais (settings.py, urls.py)
├── db.sqlite3             # Banco de dados SQLite local
├── pyproject.toml         # Configuração do projeto e dependências
├── uv.lock                # Lockfile de dependências
├── manage.py              # Utilitário CLI do Django
└── .gitignore             # Arquivo de ignorados do Git
```

---

## ⚙️ Pré-requisitos e Instalação

### 1. Clonar o repositório
```bash
git clone https://github.com/seu-usuario/agenda.git
cd agenda
```

### 2. Configurar o Ambiente Virtual e Instalar Dependências

**Se estiver utilizando o uv:**
```bash
uv sync
```

**Se estiver utilizando o pip padrão:**
```bash
python -m venv .venv
source .venv/bin/activate
pip install django>=6.0.4
```

---

## 🔐 Configuração de Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```text
SECRET_KEY=sua-chave-secreta-aqui
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

⚠️ **Importante:** não comite o arquivo `.env` nem o banco `db.sqlite3` em repositórios públicos.

---

## 🗄️ Banco de Dados e Migrações

Aplique as migrações para criar as tabelas necessárias:

```bash
python manage.py migrate
```

Crie um superusuário para acessar o painel administrativo:

```bash
python manage.py createsuperuser
```

---

## 🏃‍♂️ Executando a Aplicação

Inicie o servidor de desenvolvimento:

```bash
python manage.py runserver
```

Acesse no navegador:
👉 http://127.0.0.1:8000 

👉 Painel administrativo: http://127.0.0.1:8000/admin

---

## 📄 Licença

Este projeto está sob a licença MIT.

---

Dev Gleice Avelino
