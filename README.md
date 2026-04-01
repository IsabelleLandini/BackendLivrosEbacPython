# 📚 Backend de Livros - FastAPI

> API REST para gerenciamento de livros com autenticação e paginação.

Projeto desenvolvido para fins de estudo e portfólio.

API REST desenvolvida em Python para gerenciamento de um catálogo de livros.
Permite realizar operações completas de CRUD (Create, Read, Update, Delete) com autenticação básica.

---

## Sobre o projeto

Este projeto foi desenvolvido com o objetivo de praticar conceitos de backend, incluindo:

* Criação de APIs com FastAPI
* Integração com banco de dados usando SQLAlchemy
* Validação de dados com Pydantic
* Autenticação com HTTP Basic
* Paginação de resultados

---

## Tecnologias

* Python 3.11+
* FastAPI
* SQLAlchemy
* SQLite
* Pydantic
* Docker

---

## Funcionalidades

* Listar livros (com paginação)
* Adicionar novos livros
* Atualizar informações de livros
* Deletar livros
* Autenticação básica (usuário e senha)

---

## Autenticação

A API utiliza **HTTP Basic Auth**.
As credenciais devem ser definidas via variáveis de ambiente.

---

## Como rodar o projeto (sem Docker)

### 1. Clone o repositório:

```bash
git clone https://github.com/IsabelleLandini/books-api-fastapi.git
cd books-api-fastapi
```

### 2. Crie um ambiente virtual

```bash
python -m venv venv
```

### 3. Ative o ambiente virtual

**Windows**

```bash
venv\Scripts\activate
```

**Linux/Mac**

```bash
source venv/bin/activate
```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

### 5. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
MEU_USUARIO=admin
MINHA_SENHA=1234
DATABASE_URL=sqlite:///./livros.db
```

### 6. Execute a aplicação

```bash
uvicorn main:app --reload
```

---

## 🐳 Como rodar com Docker

```bash
docker-compose up --build
```

---

## Acessando a API

* Swagger:
  http://127.0.0.1:8000/docs

* Redoc:
  http://127.0.0.1:8000/redoc

---

## 👩‍💻 Autora

Desenvolvido por Isabelle Landini























