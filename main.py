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

#vamos caessar nosso endpoint
#vamos acessar os PATH´s 

#Path ou Rota

#200 300 400 500

#fabrica -> lojista -> consumidor

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel 
from typing import Optional

app = FastAPI()

meus_livrozinhos = {}

class Livro(BaseModel):
    nome_livro: str
    autor_livro: str
    ano_livro: int

@app.get("/")
def hello_world():
    return {"Hello": "world!"}

@app.get("/livros")
def get_livros():
    if not meus_livrozinhos:
        return{"message": "não existe nenhum livro"}
    else:
        return{"Livros": meus_livrozinhos}

@app.post("/adiciona")
def post_livros(id_livro: int, livro: Livro):
    if id_livro in meus_livrozinhos:
        raise HTTPException(status_code=400, detail= "Esse livro já existe")
    else:
        meus_livrozinhos[id_livro]= livro.dict()
        return {"message": "O livro foi criado com sucesso!"}

#fabrica -> tenis que precisa ser mudado de cor
# 1- qual é o tenis -> id_livro
#2- pegar o tenis -> pegar o livro -> id_livro
#3- processo de pintura para mudar a cor -> atualização das informações do livro

@app.put("/atualiza/{id_livro}")
def put_livros (id_livro= int, livro= Livro):
    meu_livro= meus_livrozinhos.get(id_livro)
    if not meu_livro:
        raise HTTPException(status_code=404, detail= "Esse livro não foi encontrado.")
    else:
        meu_livro[id_livro]= livro.dict()    
        return {"messafe": "As infirmações do seu livro foram atualizadad com sucesso!"}

@app.delete("/deletar/{id_livro}")
def delete_livro (id_livro:int):
    if id_livro not in meus_livrozinhos:
        raise HTTPException(status_code= 404, detail= "Esse livro não foi encontrado")
    else:
        del meus_livrozinhos[id_livro]
        return {"message": "Seu livro foi deletado com sucesso!"}
