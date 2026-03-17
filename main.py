#API de livros

#GET, POST, PUT, DELETE

#POST - adicionar novos livros (Create)
#GET- buscar os dados dos livros (Read)
#PUT - atualizar informações dos livros (Update)
#DELETE - deletar informações dos livros (Delete)

#CRUD

#Create
#Read
#Update
#Delete

#vamos acessar nosso endpoint
#vamos acessar os PATH´s 

#Path ou Rota

#200 300 400 500

#fabrica -> lojista -> consumidor
#documentaçãp swagger -> documentar os endpoints da nossa aplicação (da nossa API)

from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel 
from typing import Optional
import secrets



#criar o banco de dados local
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, Session


DATABASE_URL = "sqlite:///./livros.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


app = FastAPI(
    title= "API de livros",
    description= "API para gerenciar catalogo de livros.",
    version="1.0.0",
    contact={
        "name": "Isabelle Landini",
        "email": "isa_landini@hotmail.com"
    } 
)

MEU_USUARIO = "admin"
MINHA_SENHA = "admin"

security = HTTPBasic() 

meus_livrozinhos = {}

class LivroDB(Base): #tabela do banco de dados
    __tablename__ = "livros"
    id= Column(Integer, primary_key=True, index=True)
    nome_livro=Column(String, index=True)
    autor_livro=Column(String, index=True)
    ano_livro=Column(Integer)

class Livro(BaseModel):
    nome_livro: str
    autor_livro: str
    ano_livro: int


Base.metadata.create_all(bind=engine)

def sessao_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def autenticar_meu_usuario(credentials: HTTPBasicCredentials = Depends(security)):
    is_username_correct = secrets.compare_digest(credentials.username, MEU_USUARIO)
    is_password_correct = secrets.compare_digest(credentials.password, MINHA_SENHA)

    if not (is_username_correct and is_password_correct):
        raise HTTPException(
            status_code=401,
            detail= "Usuario ou senha incorretos",
            headers={"WWW-Authenticate": "Basic"}
        )

    return credentials


@app.get("/")
def hello_world():
    return {"Hello": "world!"}

@app.get("/livros")
def get_livros(page: int =1, limit: int =10, db: Session = Depends(sessao_db), credentials: HTTPBasicCredentials = Depends (autenticar_meu_usuario)):
    if page <1 or limit <1:
        raise HTTPException (status_code=400, detail="Page e limit estão com valores invalidos.")
    
    livros = db.query(LivroDB).offset((page -1) * limit).limit(limit).all()
    
    if not livros:
        return {"message": "Não existe nenhum livro!"}
    
    #livros_paginados = [
        # {"id": id_livro, "nome_livro": livro_data["nome_livro"], "autor_livro": livro_data["autor_livro"],"ano_livro": livro_data["ano_livro"]}
        #for id_livro, livro_data in livros_ordenados[start:end]
    #]

    total_livros = db.query(LivroDB).count()

    return {
        "page": page,
        "limit": limit, 
        "total": total_livros, 
        "livros": [{"id": livro.id, "nome_livro": livro.nome_livro, "autor_livro": livro.autor_livro, "ano_livro": livro.ano_livro} for livro in livros]
        }

@app.post("/adiciona")
def post_livros(livro: Livro, db: Session = Depends(sessao_db), credentials: HTTPBasicCredentials = Depends(autenticar_meu_usuario)):
    db_livro = db.query(LivroDB).filter(LivroDB.nome_livro == livro.nome_livro, LivroDB.autor_livro == livro.autor_livro).first()
    if db_livro:
        raise HTTPException(status_code=400, detail="Esse livro já existe no catálogo.")
    novo_livro = LivroDB(nome_livro=livro.nome_livro, autor_livro=livro.autor_livro, ano_livro=livro.ano_livro)
    db.add(novo_livro)
    db.commit()
    db.refresh(novo_livro)
    return {"message": "Livro adicionado com sucesso!"}

#fabrica -> tenis que precisa ser mudado de cor
# 1- qual é o tenis -> id_livro
#2- pegar o tenis -> pegar o livro -> id_livro
#3- processo de pintura para mudar a cor -> atualização das informações do livro
# dicionario = hasmap
# chave - valor
@app.put("/atualiza/{id_livro}")
def put_livros (id_livro: int, livro: Livro, db: Session = Depends(sessao_db), credentials: HTTPBasicCredentials = Depends(autenticar_meu_usuario)):
    db_livro = db.query(LivroDB).filter(LivroDB.id== id_livro).first()
    if not db_livro:
        raise HTTPException(status_code=404,detail= "Este livro não foi encontrado no seu banco de dados!" )
    db_livro.nome_livro = livro.nome_livro #atualização atraves do body
    db_livro.autor_livro = livro.autor_livro
    db_livro.ano_livro = livro.ano_livro
    db.commit()
    db.refresh(db_livro)

    return {'message': 'O livro foi atualizado com sucesso!'}


@app.delete("/deletar/{id_livro}")
def delete_livro (id_livro:int, db:Session = Depends(sessao_db), credentials: HTTPBasicCredentials = Depends(autenticar_meu_usuario)):
    db_livro = db.query(LivroDB).filter(LivroDB.id == id_livro).first() #verifica se existe

    if not db_livro:
        raise HTTPException(status_code= 404, detail= "Esse livro não foi encontrado no seu banco de dados!")
    
    db.delete(db_livro)
    db.commit()

    return {"message": "Seu livro foi deletado com sucesso!"}


    

    

    