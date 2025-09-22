#Implementar um programa em Python que gerencia tarefas, permitindo adicionar, listar, remover e marcar tarefas como concluídas, seguindo um menu interativo.

#criar um dicionario para armazenar as tarefas
# Variável global de tarefas
tarefas = {}

def adicionar_tarefa(nome):
    nome = nome.strip()
    if nome in tarefas:
        return "Essa tarefa já existe."
    else:
        tarefas[nome] = False   
        return (f"Tarefa '{nome}' adicionada com sucesso!!")

def listar_tarefas(tarefas):
    if not tarefas:
        return "Nenhuma tarefa cadastrada."
    else:
        resultado = ["Lista de tarefas"]
        for nome, concluida in sorted(tarefas.items(), key=lambda item: item[0]):
            status = "✅ Concluída" if "Concluida" else "❌ não concluída"
            resultado.append(f"{nome}: {status}") 
        return "\n".join(resultado)

def remover_tarefa(nome):
    if nome in tarefas:
        del tarefas[nome]
        return (f"Tarefa '{nome}' removida com sucesso!")
    else:
        return ("Erro: Tarefa não encontrada.")

def marcar_concluida(nome):
    nome = nome.strip()
    if nome in tarefas:
        tarefas[nome] = True
        return (f"Tarefa '{nome}' marcada como concluída!")
    else:
        tarefas[nome]= False
        return (f"Erro: Tarefa não encontrada.")

def exibir_menu():
    return (
        """Menu:\n 
        1 - Adicionar tarefa \n 
        2 - Listar tarefa s\n 
        3 - Remover tarefa \n 
        4 - Marcar tarefa como concluída \n 
        5 - Sair""" 
    )

def main():
    while True:
        print(exibir_menu())
        opcao = input ("Escolha uma opção (1-5): ").strip()
        if opcao == 1:
            nome = input("Adicionar tarefa: ") 
            print(adicionar_tarefa(nome))
        elif opcao == 2:
            print(listar_tarefas(tarefas))
        elif opcao == 3:
            nome = input("Remover tarefa ")
            print(remover_tarefa(nome))
        elif opcao == 4:
            nome = input("Marcar tarefa como concluída ")
            print(marcar_concluida(nome))
        elif opcao == 5:
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "main":
    main()
