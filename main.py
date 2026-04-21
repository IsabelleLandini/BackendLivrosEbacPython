# ========================================
#         API DE LIVROS - FastAPI
# ========================================

from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
# Validação de dados
from pydantic import BaseModel 
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker, Session
# Segurança para comparar credenciais
import secrets
# Variáveis de ambiente
import os
import json
import redis
from dotenv import load_dotenv


#==============================
#    CONFIGURAÇÕES INICIAIS
#==============================
# URL do banco vinda do .env
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
# Usuário e senha vindos do .env
MEU_USUARIO = os.getenv("MEU_USUARIO")
MINHA_SENHA = os.getenv("MINHA_SENHA")

#============================
#       BANCO DE DADOS
#============================
# Criação da engine de conexão
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
# Criação da sessão do banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base para criação das tabelas
Base = declarative_base()

#============================
#    REDIS (com proteção)
#============================
try:
    redis_client = redis.Redis(
        host='localhost', 
        port=6379, 
        db=0, 
        decode_responses=True
    )
    redis_client.ping()
    print('Redis conectado com sucesso!')
except Exception as e:
    print('Erro ao conectar no Redis:', e)
    redis_client = None

#===========
#    APP
#===========
# Configuração da API
app = FastAPI(
    title= "API de livros",
    description= "API para gerenciar catálogo de livros.",
    version="1.0.0",
    contact={
        "name": "Isabelle Landini",
        "email": "isa_landini@hotmail.com"
    } 
)
# Instância de segurança
security = HTTPBasic() 

#===============
#    MODELOS
#===============

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

#=====================
#    FUNÇÕES REDIS
#=====================

# Funções utilitárias para o cache
async def salvar_livros_redis(livros: list):
    if not redis_client:
        return
    try:
        redis_client.setex('livros', 30, json.dumps(livros))
    except Exception as e:
        print('Erro ao salvar no Redis:', e)

async def deletar_livros_redis():
    if not redis_client:
        return
    try:
        redis_client.delete('livros')
    except Exception as e:
        print('Erro ao deletar no Redis:', e)

#====================
#    DEPENDÊNCIAS
#====================

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

#=============
#    ROTAS
#=============

@app.get("/")
def hello_world():
    """
    Rota inicial para teste da API
    """
    return {"Hello": "world!"}

@app.get('/debug/redis')
def ver_livros_redis():
    if not redis_client:
        return {'erro': 'Redis não está disponível'}
    try:
        valor = redis_client.get('livros')
        ttl = redis_client.ttl('livros')

        return {
            'chave': 'livros',
            'valor': json.loads(valor) if valor else None,
            'ttl': ttl
        }

    except Exception as e:
        return{'erro': str(e)}

@app.get("/livros")
async def get_livros(
    db: Session = Depends(sessao_db), 
    credentials: HTTPBasicCredentials = Depends (autenticar_meu_usuario)):
    """
    Lista livros com paginação
    """
    try:
        cached = redis_client.get('livros') if redis_client else None
    except Exception as e:
        print('Erro no Redis (GET):', e)
        cached = None
    if cached:
        return json.loads(cached)
    
    # Busca no banco
    livros = db.query(LivroDB).all()
    # Caso não existam livros
    if not livros:
        return {"message": "Não existe nenhum livro!"}
    # Retorno estruturado
    resposta = [
        {
        "id": livro.id, 
        "nome_livro": livro.nome_livro,
        "autor_livro": livro.autor_livro, 
        "ano_livro": livro.ano_livro
        } for livro in livros
    ]
    # Salva no cache
    await salvar_livros_redis(resposta)
   
    return resposta

@app.post("/livros")
async def adicionar_livro(
    livro: Livro, 
    db: Session = Depends(sessao_db), 
    credentials: HTTPBasicCredentials = Depends(autenticar_meu_usuario)):
    """
    Adiciona um novo livro ao banco
    """
    
    # Verifica duplicidade
    db_livro = db.query(LivroDB).filter(
        LivroDB.nome_livro == livro.nome_livro, 
        LivroDB.autor_livro == livro.autor_livro
        ).first()
    if db_livro:
        raise HTTPException(status_code=400, detail="Livro já existe.")
    # Cria novo livro
    novo_livro = LivroDB(**livro.model_dump())
   
    db.add(novo_livro)
    db.commit()
    db.refresh(novo_livro)
    # invalida cache
    await deletar_livros_redis()

    return {"message": "Livro adicionado com sucesso!"}

@app.put("/livros/{id_livro}")
async def atualizar_livros (
    id_livro: int, 
    livro: Livro, 
    db: Session = Depends(sessao_db), 
    credentials: HTTPBasicCredentials = Depends(autenticar_meu_usuario)):
    """
    Atualiza um livro existente
    """
    db_livro = db.query(LivroDB).filter(LivroDB.id== id_livro).first()
    if not db_livro:
        raise HTTPException(status_code=404,detail= "Livro não encontrado." )
    # Atualização dos campos
    db_livro.nome_livro = livro.nome_livro #atualização atraves do body
    db_livro.autor_livro = livro.autor_livro
    db_livro.ano_livro = livro.ano_livro

    db.commit()
    # invalida cache
    await deletar_livros_redis()
   
    return {'message': 'Livro atualizado com sucesso!'}

@app.delete("/livros/{id_livro}")
async def deletar_livro (
    id_livro:int, 
    db:Session = Depends(sessao_db), 
    credentials: HTTPBasicCredentials = Depends(autenticar_meu_usuario)):
    """
    Remove um livro do banco
    """
    db_livro = db.query(LivroDB).filter(LivroDB.id == id_livro).first() #verifica se existe

    if not db_livro:
        raise HTTPException(status_code= 404, detail= "Livro não encontrado.")
    
    db.delete(db_livro)
    db.commit()

    # invalida cache
    await deletar_livros_redis()

    return {"message": "Livro deletado com sucesso!"}


    

    

    