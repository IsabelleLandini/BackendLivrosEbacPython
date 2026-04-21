# =========================================
# API de Livros - FastAPI
# =========================================

# Importações principais do FastAPI
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
# Validação de dados
from pydantic import BaseModel 
# Tipagem
from typing import Optional
# Segurança para comparar credenciais
import secrets
# Variáveis de ambiente
import os
from dotenv import load_dotenv

# Configuração do Banco de Dados (SQLite)
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, Session


import asyncio
# URL do banco vinda do .env
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

# Criação da engine de conexão
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Criação da sessão do banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base para criação das tabelas
Base = declarative_base()

# Configuração da API
app = FastAPI(
    title= "API de livros",
    description= "API para gerenciar catalogo de livros.",
    version="1.0.0",
    contact={
        "name": "Isabelle Landini",
        "email": "isa_landini@hotmail.com"
    } 
)
# Autenticação básica (HTTP Basic)

# Usuário e senha vindos do .env
MEU_USUARIO = os.getenv("MEU_USUARIO")
MINHA_SENHA = os.getenv("MINHA_SENHA")

# Instância de segurança
security = HTTPBasic() 

meus_livrozinhos = {}
livros = []
id_counter = 1

# Modelos do Banco (SQLAlchemy)
class LivroDB(Base): 
    """
    Representa a tabela 'livros' no banco de dados
    """
    __tablename__ = "livros"
    id= Column(Integer, primary_key=True, index=True)
    nome_livro=Column(String, index=True)
    autor_livro=Column(String, index=True)
    ano_livro=Column(Integer)

# Modelos de Entrada (Pydantic)
class Livro(BaseModel):
    """
    Modelo utilizado para validar os dados recebidos na API
    """
    nome_livro: str
    autor_livro: str
    ano_livro: int

# Cria as tabelas no banco (caso não existam)
Base.metadata.create_all(bind=engine)

# Dependência do banco de dados
def sessao_db():
    """
    Cria e encerra uma sessão com o banco de dados
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Função de autenticação
def autenticar_meu_usuario(credentials: HTTPBasicCredentials = Depends(security)):
    """
    Valida usuário e senha utilizando comparação segura
    """
    is_username_correct = secrets.compare_digest(credentials.username, MEU_USUARIO)
    is_password_correct = secrets.compare_digest(credentials.password, MINHA_SENHA)

    if not (is_username_correct and is_password_correct):
        raise HTTPException(
            status_code=401,
            detail= "Usuario ou senha incorretos",
            headers={"WWW-Authenticate": "Basic"}
        )

    return credentials

    
# Rotas da API
@app.get("/")
def hello_world():
    """
    Rota inicial para teste da API
    """
    return {"Hello": "world!"}

async def chamadas_externas_1():
   await asyncio.sleep(2)
   return "Resultado chamada externa 1"

async def chamadas_externas_2():
   await asyncio.sleep(2)
   return "Resultado chamada externa 2"

async def chamadas_externas_3():
   await asyncio.sleep(2)
   return "Resultado chamada externa 3"


@app.get("/chamadas-externas")
async def chamadas_externas():
    tarefa1 = asyncio.create_task(chamadas_externas_1())
    tarefa2 = asyncio.create_task(chamadas_externas_2())
    tarefa3 = asyncio.create_task(chamadas_externas_3())

    resultado1 = await tarefa1
    resultado2 = await tarefa2
    resultado3 = await tarefa3

    return {
        "message": "Todas as chamadas nas API's foram concluidas com sucesso",
        "resultado": [resultado1, resultado2, resultado3]
        }

# GET - Listar livros (Assíncrono)
@app.get("/livros")
async def get_livros():
    await asyncio.sleep(1)
    return livros

# POST - Criar livro (Assíncrono)
@app.post("/livros")
async def criar_livro(livro: Livro):
    # Gera ID incremental para novo livro
    global id_counter
    # Simula chamada externa assíncrona
    await asyncio.sleep(2)
    novo_livro = {
        'id': id_counter,
        'nome_livro': livro.nome_livro,
        'autor_livro': livro.autor_livro,
        'ano_livro': livro.ano_livro}
    
    livros.append(novo_livro)
    id_counter += 1

    return novo_livro

# PUT - Atualizar livro (Assíncrono)
@app.put("/livros/{id_livro}")
async def atualizar_livro (id_livro: int, livro: Livro):
    await asyncio.sleep(2)
    # Busca livro pelo ID
    for item in livros:
        if item['id'] == id_livro:
            item['nome_livro'] = livro.nome_livro
            item['autor_livro'] = livro.autor_livro
            item['ano_livro'] = livro.ano_livro
            return item
    raise HTTPException(status_code=404, detail='Livro não encontrado')

# DELETE - Remover livro (Assíncrono)
@app.delete("/livros/{id_livro}")
async def delete_livro (id_livro:int):
    await asyncio.sleep(2)
    for index, item in enumerate(livros):
        if item['id'] == id_livro:
            removido = livros.pop(index)
            return {'message': 'Livro removido com sucesso', 'livro': removido}
    raise HTTPException(status_code= 404, detail= 'Livro não encontrado')
    

    

    