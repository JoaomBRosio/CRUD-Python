
# "CRUD" Python 🚀

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-2.0+-blue?logo=flask)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue?logo=postgresql)

Um simples sistema de gerenciamento de usuários construído em Python usando Flask e PostgreSQL, para melhor compreensão da linguagem e bibliotecas! Este projeto permite cadastro, edição, autenticação e logout de usuários. A interface é feita em HTML com templates para interação com o backend. 🖥️

## Funcionalidades Principais 🛠️

- **Cadastro de usuários**: Permite que novos usuários se cadastrem no sistema.
- **Login e Autenticação**: Verifica o login de cada usuário.
- **Edição de Dados**: Permite que usuários atualizem seu nome, email e senha.
- **Dashboard e Logout**: Após o login, o usuário acessa um dashboard e pode fazer logout com facilidade.

## Como Iniciar o Projeto ⚙️

1. **Clone este repositório**: `git clone https://github.com/seu-usuario/nome-do-repositorio.git`
2. **Instale as dependências**:
   ```bash
   pip install Flask psycopg2
   ```
3. **Configure seu banco de dados PostgreSQL** com as informações corretas no código.
4. **Execute a aplicação**:
   ```bash
   python app.py
   ```

## Bibliotecas Utilizadas 📚

- **Flask**: Framework web para Python, usado para criar rotas, gerenciar sessões e renderizar templates HTML. Ideal para criar aplicativos web leves e rápidos.
- **psycopg2**: Biblioteca que faz a conexão do Python com o banco de dados PostgreSQL, realizando consultas SQL e executando operações de CRUD (criar, ler, atualizar e excluir).

## Estrutura do Projeto 📂

```
/project-root
├── app.py                   # Arquivo principal da aplicação
├── models.py                # Código que faz a conexão e as operações com o banco de dados
├── templates/
│   ├── login.html           # Formulário de login
│   ├── cadastro.html        # Formulário de cadastro
│   ├── editar.html          # Formulário de edição de perfil
│   └── dashboard.html       # Painel principal após o login
└── README.md                # Documentação do projeto
```

## Consumo em HTML 🖼️

Os templates HTML foram projetados para facilitar a interação com o backend. As rotas para cada página estão configuradas com o `Flask`, tornando as operações dinâmicas e reativas. Exemplos de páginas HTML:

- `login.html` → Página de login para autenticação.
- `cadastro.html` → Formulário de cadastro de novos usuários.
- `editar.html` → Formulário de edição de informações do usuário.
- `dashboard.html` → Painel principal do usuário autenticado.
