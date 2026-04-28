# 📚 Backend de Livros - FastAPI + Redis + Celery + Kafka

> API REST desenvolvida em Python para gerenciamento de um catálogo de livros, com foco em performance e processamento assíncrono.

Projeto desenvolvido para fins de estudo e portfólio.

---

## Sobre o projeto

Esta API permite realizar operações completas de CRUD (Create, Read, Update, Delete) em um catálogo de livros, com:

* Autenticação básica
* Cache com Redis
* Processamento assíncrono com Celery
* Integração com Kafka para mensageria

O projeto aplica boas práticas de desenvolvimento backend, incluindo separação de responsabilidades, uso de filas e otimização de performance.

---

## Conceitos Aplicados

* API REST com FastAPI
* Integração com banco de dados (SQLAlchemy)
* Cache com Redis
* Invalidação de cache
* Processamento assíncrono com Celery
* Fila de tarefas com Redis (broker)
* Mensageria com Kafka
* Programação assíncrona (`async/await`)
* Autenticação HTTP Basic
* Containerização com Docker/Podman

---

## Tecnologias

* Python 3.11+
* FastAPI
* Uvicorn
* SQLAlchemy
* Redis
* Celery
* Kafka
* Docker / Podman
* python-dotenv

---

## Funcionalidades

### Livros

* Listar livros (com cache Redis)
* Adicionar novos livros
* Atualizar livros existentes
* Deletar livros

### Assíncrono (Celery)

* Cálculo de soma em background
* Cálculo de fatorial em background
* Consulta do status das tarefas

---

## Processamento Assíncrono (Celery + Redis)

A API utiliza o Celery para executar tarefas pesadas em background, evitando bloquear a aplicação principal.

### Tarefas disponíveis

- `POST /calcular_soma` → executa soma assíncrona
- `POST /calcular_fatorial` → executa cálculo de fatorial

### Fluxo das tarefas

Cliente → FastAPI → Redis (broker) → Celery Worker → Resultado

### Status das tarefas

- `PENDING` → aguardando execução
- `STARTED` → em execução
- `SUCCESS` → concluída
- `FAILURE` → erro na execução

---

## Como funciona o cache

* O endpoint `GET /livros`:

  * Primeiro verifica se os dados estão no Redis
  * Se estiverem → retorna do cache (mais rápido)
  * Se não → busca no banco, salva no Redis e retorna

### Configuração

- Chave: `livros`
- TTL: **30 segundos**

### Invalidação automática

O cache é apagado quando:
- Um livro é criado
- Um livro é atualizado
- Um livro é deletado

---

## 🐳 Executando com Docker / Podman (RECOMENDADO)

Este projeto utiliza múltiplos serviços (API, Redis, Celery, Kafka e Kafka UI).

### Subir o ambiente completo

```bash
podman machine start
podman-compose up -d --build
```

### Serviços disponíveis

* API → http://localhost:8000
* Kafka UI → http://localhost:8080
* Redis → localhost:6379
* Kafka → localhost:9092

---

## Kafka UI

Acesse:

http://localhost:8080

* Cluster: `local`
* Visualização de:

  * Brokers
  * Topics
  * Mensagens

---

## Executando o Celery Worker

```bash
celery -A celery_app worker --loglevel=info
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
pip install fastapi uvicorn sqlalchemy redis python-dotenv celery
```

---

### 5. Configure o arquivo `.env`

```env
DATABASE_URL=sqlite:///./livros.db
MEU_USUARIO=admin
MINHA_SENHA=1234
REDIS_HOST=localhost
REDIS_PORT=6379
KAFKA_SERVER=localhost:9092
```

---

### 6. Execute a API

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

* GET /livros
* POST /livros
* PUT /livros/{id_livro}
* DELETE /livros/{id_livro}

### Tarefas Assíncronas

* POST /calcular_soma
```bash 
/calcular_soma?a=5&b=10
```

* POST /calcular_fatorial
```bash
/calcular_fatorial?n=5
```

* GET /tarefas/recentes
Lista as tarefas com:
* ID
* Status
* Resultado

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

## Arquitetura

O sistema é composto por:

* FastAPI → API principal
* Redis → cache e broker do Celery
* Celery → processamento assíncrono
* Kafka → mensageria
* Kafka UI → monitoramento

Fluxo geral:

Cliente → API → Redis/Kafka → Worker → Resultado

---

## 👩‍💻 Autora

Desenvolvido por Isabelle Landini
