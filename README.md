# 📚 Backend de Livros - FastAPI

> Esta API foi desenvolvida utilizando FastAPI, SQLAlchemy e Redis com o objetivo de gerenciar um catálogo de livros e otimizar a performance através de cache.

Projeto desenvolvido para fins de estudo e portfólio.

API REST desenvolvida em Python para gerenciamento de um catálogo de livros.
Permite realizar operações completas de CRUD (Create, Read, Update, Delete) com autenticação básica.
O Redis é utilizado para armazenar temporariamente a lista de livros, reduzindo consultas repetidas ao banco de dados e melhorando o tempo de resposta da aplicação.

---

## Sobre o projeto

Este projeto foi desenvolvido com o objetivo de praticar conceitos de backend, incluindo:

* Criação de APIs com FastAPI
* Integração com banco de dados utilizando SQLAlchemy
* Uso de Redis como cache
* Programação assíncrona com `async` e `await`
* Estruturação de CRUD completo
* Otimização de performance com cache

---

## Tecnologias

* Python 3.11+
* FastAPI
* Uvicorn
* SQLAlchemy
* Redis
* python-dotenv

---

## Funcionalidades

* Listar livros (com cache Redis)
* Adicionar novos livros
* Atualizar livros existentes
* Deletar livros
* Autenticação HTTP Basic
* Cache com expiração automática (TTL)
* Invalidação de cache ao alterar dados

---

## Como funciona o cache

* O endpoint `GET /livros`:

  * Primeiro verifica se os dados estão no Redis
  * Se estiverem → retorna do cache (mais rápido)
  * Se não → busca no banco, salva no Redis e retorna

* O cache:

  * Utiliza a chave `'livros'`
  * Possui TTL de **30 segundos**

* O cache é automaticamente invalidado quando:

  * Um livro é criado
  * Um livro é atualizado
  * Um livro é deletado

---

## Executando o Redis

### ✔️ Opção 1: Local

```bash
redis-server
```

### ✔️ Opção 2: Docker

```bash
docker run -d -p 6379:6379 redis
```

---

## Como rodar o projeto (sem Docker)

### 1. Clone o repositório

```bash
git clone https://github.com/IsabelleLandini/books-api-fastapi.git
cd books-api-fastapi
```

---

### 2. Crie um ambiente virtual

```bash
python -m venv venv
```

---

### 3. Ative o ambiente virtual

**Windows**

```bash
venv\Scripts\activate
```

**Linux/Mac**

```bash
source venv/bin/activate
```

---

### 4. Instale as dependências

```bash
pip install fastapi uvicorn sqlalchemy redis python-dotenv
```

---

### 5. Configure o arquivo `.env`

```env
DATABASE_URL=sqlite:///./livros.db
MEU_USUARIO=admin
MINHA_SENHA=1234
```

---

### 6. Execute a aplicação

```bash
uvicorn main:app --reload
```

---

## Acessando a API

* Swagger: http://127.0.0.1:8000/docs
* Redoc: http://127.0.0.1:8000/redoc

---

## 🔐 Autenticação

A API utiliza **HTTP Basic Auth**.

Exemplo:

* Usuário: `admin`
* Senha: `1234`

---

## Endpoints

### 🔹 GET /livros

Lista todos os livros (utilizando cache Redis).

---

### 🔹 POST /livros

Cria um novo livro.

Exemplo de body:

```json
{
  "nome_livro": "Dom Casmurro",
  "autor_livro": "Machado de Assis",
  "ano_livro": 1899
}
```

---

### 🔹 PUT /livros/{id_livro}

Atualiza um livro existente.

---

### 🔹 DELETE /livros/{id_livro}

Remove um livro pelo ID.

---

### 🔹 GET /debug/redis

Exibe o conteúdo do cache e o tempo restante (TTL).

---

## Exemplos de teste (curl)

### Listar livros

```bash
curl -u admin:1234 http://127.0.0.1:8000/livros
```

---

### Adicionar livro

```bash
curl -X POST -u admin:1234 http://127.0.0.1:8000/livros \
-H "Content-Type: application/json" \
-d "{\"nome_livro\":\"Teste\",\"autor_livro\":\"Autor\",\"ano_livro\":2024}"
```

---

### Atualizar livro

```bash
curl -X PUT -u admin:1234 http://127.0.0.1:8000/livros/1 \
-H "Content-Type: application/json" \
-d "{\"nome_livro\":\"Atualizado\",\"autor_livro\":\"Autor\",\"ano_livro\":2025}"
```

---

### Deletar livro

```bash
curl -X DELETE -u admin:1234 http://127.0.0.1:8000/livros/1
```

---

## Testando o cache

1. Faça uma requisição:

   ```
   GET /livros
   ```

2. Faça novamente:

   * A segunda resposta será mais rápida (vem do Redis)

3. Verifique:

   ```
   GET /debug/redis
   ```

---

## Conceitos aplicados

* API REST com FastAPI
* Integração com banco de dados (SQLAlchemy)
* Uso de Redis como cache
* Invalidação de cache
* Autenticação básica
* Programação assíncrona (`async/await`)

---

## 👩‍💻 Autora

Desenvolvido por Isabelle Landini
