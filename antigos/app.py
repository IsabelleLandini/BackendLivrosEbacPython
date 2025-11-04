#crie uma aplicação fastapi
from fastapi import FastAPI, HTTPException

app = FastAPI() 
#definindo uma lista de tarefas
minhas_tarefas = []
#cada tarefa sera representada como um dicionario

#rota para add uma tarefa
@app.post("/adiciona")
def post_tarefas (id_tarefa: int, nome_tarefa: str, descricao: str):
    for tarefa in minhas_tarefas:
        if tarefa["id_tarefa"] == id_tarefa:
            raise HTTPException(status_code = 400, detail= "Essa tarefa já existe.")
    nova_tarefa = {
        "id_tarefa": id_tarefa,
        "nome_tarefa": nome_tarefa,
        "descricao": descricao,
        "concluida": False
    }
    minhas_tarefas.append(nova_tarefa)
    return {"message": "Tarefa adicionada com sucesso!"}

#Rota para Listar as Tarefas
@app.get("/tarefas")
def get_tarefas():
    if not minhas_tarefas:
        return {"message": "Não existe nenhuma tarefa"}
    else:
        return {"tarefas": minhas_tarefas}
    
#Rota para Marcar uma Tarefa como Concluída
@app.put("/atualiza/{id_tarefa}/concluida")
def put_tarefas(id_tarefa: int, nome_tarefa: str = None, descricao: str = None, concluida: bool = False):
    for tarefa in minhas_tarefas:
        if tarefa["id_tarefa"] == id_tarefa:
            if nome_tarefa:
                tarefa["nome_tarefa"] = nome_tarefa    
            if descricao:
                tarefa["descricao"] = descricao
            tarefa["concluida"] = concluida
            return {"message": "As informações da tarefa foram atualizadas com sucesso!"}
    raise HTTPException (status_code = 404, detail = "Essa tarefa não foi encontrada.")

#Rota para remover uma tarefa
@app.delete("/deletar/{id_tarefa}")
def delete_tarefa(id_tarefa: int):
    for i, tarefa in enumerate(minhas_tarefas):
        if tarefa["id_tarefa"] == id_tarefa:
            del minhas_tarefas[i]
            return {"message": "Sua tarefa foi deletada com sucesso!"}
    raise HTTPException(status_code=404, detail= "Essa tarefa não foi encontrada!")

#Testando a aplicação
