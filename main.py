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
import os


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

class Livro(BaseModel):
    nome_livro: str
    autor_livro: str
    ano_livro: int

def autenticar_meu_usuario(credentials: HTTPBasicCredentials = Depends(security)):
    is_username_correct = secrets.compare_digest(credentials.username, MEU_USUARIO)
    is_password_correct = secrets.compare_digest(credentials.password, MINHA_SENHA)

    if not (is_username_correct and is_password_correct):
        raise HTTPException(
            status_code=401,
            detail= "Usuario ou senha incorretos",
            headers={"WWW-Authenticate": "Basic"}
        )
@app.get("/")
def hello_world():
    return {"Hello": "world!"}

@app.get("/livros")
def get_livros(page: int =1, limit: int =10, credentials: HTTPBasicCredentials = Depends (autenticar_meu_usuario)):
    if page <1 or limit <1:
        raise HTTPException (status_code=400, detail="Page e limit estão com valores invalidos.")
    if not meus_livrozinhos:
        return {"message": "Não existe nenhum livro!"}
    
    start = (page - 1) * limit
    end = start + limit

    livros_paginados = [
        {
            "id": id_livro,
            "nome_livro": livro_data["nome_livro"],
            "autor_livro": livro_data["autor_livro"],
            "ano_livro": livro_data["ano_livro"],
        }
        for id_livro, livro_data in list(meus_livrozinhos.items())[start:end]
    ]

    return {
        "page": page,
        "limit": limit, 
        "total": len(meus_livrozinhos), 
        "livros": livros_paginados
        }


@app.post("/adiciona")
def post_livros(
    id_livro: int,
    livro: Livro,
    credentials: HTTPBasicCredentials = Depends(autenticar_meu_usuario) 
):
    if id_livro in meus_livrozinhos:
        raise HTTPException(status_code=400, detail= "Esse livro já existe")
    else:
        meus_livrozinhos[id_livro]= livro.dict()
        return {"message": "O livro foi criado com sucesso!"}

#fabrica -> tenis que precisa ser mudado de cor
# 1- qual é o tenis -> id_livro
#2- pegar o tenis -> pegar o livro -> id_livro
#3- processo de pintura para mudar a cor -> atualização das informações do livro
# dicionario = hasmap
# chave - valor
@app.put("/atualiza/{id_livro}")
def put_livros (
    id_livro: int,
    livro: Livro, 
    credentials: HTTPBasicCredentials = Depends(autenticar_meu_usuario)
):
    meu_livro= meus_livrozinhos.get(id_livro) # aqui p meu_livro recebe o valor e vira um hashmap(dicionario)
    if not meu_livro:
        raise HTTPException(status_code=404, detail= "Esse livro não foi encontrado.")
    else:
        #jogo a informação dentro do meu antigo dicionario(que é meus_livrozinhos)
        # e NÃO  dentro da REFERENCIA do antigo dicionário
        # antigo dicionario !=(diferente) Referencia do antigo dicionario
        meus_livrozinhos[id_livro]= livro.dict()    # com o dict cria um novo hashmap/dicionario
        return {"message": "As informações do seu livro foram atualizadad com sucesso!"}

@app.delete("/deletar/{id_livro}")
def delete_livro (
    id_livro:int,
    credentials: HTTPBasicCredentials = Depends(autenticar_meu_usuario)
):
    if id_livro not in meus_livrozinhos:
        raise HTTPException(status_code= 404, detail= "Esse livro não foi encontrado")
    else:
        del meus_livrozinhos[id_livro]
        return {"message": "Seu livro foi deletado com sucesso!"}
    