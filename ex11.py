#FastAPI funcional, implementar pydantic
#passo1
#importar Basemodel no modulo pydantic
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException

app = FastAPI()

#criar uma classe chamada tarefa que herda de basemodel
class Tarefa(BaseModel):
    nome: str
    descricao: str
    concluida: bool = False

minhas_tarefas ={}

#passo 2
#adicionar tarefa - post - recebendo um objeto do tipo tarefa como parametro
@app.post("/adiciona")
def post_tarefas(id_tarefa:int, tarefa: Tarefa):
    if id_tarefa in minhas_tarefas:
        raise HTTPException(status_code=400, detail="Essa tarefa já existe!")
    else:
        minhas_tarefas[id_tarefa]= tarefa
        return {"message": "Tarefa adicionada com sucesso!"}
    
#passo 3
#modificar a lista de tarefas para armazenar obj do tipo tarefa em vez de dicionarios

#passo 4
#listar as tarefas -get- retorne os obj da lista
#converter os obj tarefa em json automaticamente uando pydantic
@app.get("/tarefas")
def get_tarefas():
    if not minhas_tarefas:
        return {"message": "Não existe nenhuma tarefa."}
    else: 
        return {"Tarefas": minhas_tarefas}

# passo 5
# atualizar as rotas de marcar como concluida e remover tarefas para usar o campo nome do modelo pydantic

@app.put("/atualiza/{id_tarefa}")
def put_tarefas (id_tarefa: int, tarefa: Tarefa):
    minha_tarefa = minhas_tarefas.get(id_tarefa)
    if not minha_tarefa:
        raise HTTPException(status_code=404, detail= "Essa tarefa não foi encontrada.")
    else:
        minhas_tarefas[id_tarefa]= tarefa
        return {"message": "As informações da sua tarefa foram atualizadas com sucesso!"}
    
@app.delete("/deletar")
def delete_tarefa(id_tarefa: int):
    if id_tarefa not in minhas_tarefas:
        raise HTTPException( status_code=404, detail= "Essa tarefa não foi encontrada.")
    else:
        del minhas_tarefas[id_tarefa]
        return {"message": "Sua tarefa foi deletada com sucesso!"}
    


