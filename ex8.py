#Crie um programa para gerenciar uma biblioteca de livros. 
biblioteca_livros = {}
# O programa deve exibir um menu com as opções: adicionar livro, listar livros, remover livro, atualizar quantidade de livros, registrar empréstimo, exibir histórico de empréstimos e sair.
def menu():
    return """
    Menu:
    1. Adicionar livro
    2. Listar livros
    3. Remover livro
    4. Atualizar quantidade de livros
    5. Registrar empréstimo
    6. Exibir histórico de empréstimos
    7. Sair
    """

#Os livros serão armazenados em um dicionário onde a chave será o título do livro e 
#o valor será outro dicionário contendo duas informações: a quantidade de exemplares disponíveis e o nome do autor. 
# Quando o usuário escolher a opção de adicionar um livro, o programa deverá pedir o título do livro, o nome do autor e a quantidade de exemplares. Esses dados devem ser armazenados no dicionário.

def add_livro(livros):
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o nome do autor: ")
    try:
        quantidade = int(input("Digite a quantidade de exemplares: "))
    except ValueError:
        print("Erro: Digite um número válido para a quantidade.")
        return
    livros[titulo] = {"autor": autor, "quantidade": quantidade}
    print(f'Livro "{titulo}" adicionado com sucesso!')
    
#Na opção de listar livros, o programa deve exibir todos os livros cadastrados no formato: título do livro - autor - quantidade disponível. Os livros devem ser ordenados alfabeticamente por título.
def listar_livros(livros):
    if not livros:
        print("Nenhum livro cadastrado.")
    else:
        for titulo in sorted(livros.keys()):
            autor = livros[titulo]["autor"]
            quantidade = livros[titulo]["quantidade"]
            print(f"{titulo} - {autor} - {quantidade} exemplares disponíveis")
#Se o usuário escolher remover um livro, o programa deverá pedir o título do livro a ser removido e, caso ele exista, o livro será removido do dicionário. Se o livro não existir, o programa exibirá uma mensagem de erro.

def remover_livro(livros):
    titulo = input("Digite o título do livro a ser removido: ")
    if titulo in livros:
        del livros[titulo]
        print(f'Livro "{titulo}" removido com sucesso!')
    else:
        print("Erro: Livro não encontrado.")
#Para atualizar a quantidade de livros, o programa pedirá o título do livro e a nova quantidade de exemplares. Se o livro existir, a quantidade será atualizada. Caso contrário, será exibida uma mensagem de erro.

def atualizar_quantidade(livros):
    titulo = input("Digite o título do livro: ")
    if titulo in livros:
        nova_quantidade = int(input("Digite a nova quantidade de exemplares: "))
        livros[titulo]["quantidade"] = nova_quantidade
        print(f'Quantidade do livro "{titulo}" atualizada para {nova_quantidade} exemplares.')
    else:
        print("Erro: Livro não encontrado.")
#Ao registrar um empréstimo, o programa pedirá o título do livro e a quantidade de exemplares a ser emprestada. Se houver exemplares suficientes disponíveis, a quantidade do livro será atualizada e o empréstimo será registrado. Se não houver exemplares suficientes, o programa exibirá uma mensagem de erro.
#O histórico de empréstimos deve ser armazenado em uma lista, onde cada entrada consiste no título do livro e a quantidade de exemplares emprestados. Quando o usuário escolher exibir o histórico de empréstimos, o programa deve mostrar todas as entradas feitas.

historico_emprestimos = []
def registrar_emprestimo(livros, historico):
    titulo = input("Digite o título do livro a ser emprestado: ")
    if titulo in livros:
        try:
            quantidade_emprestada = int(input("Digite a quantidade de exemplares a ser emprestada: "))
        except ValueError:
            print("Erro: Digite um número válido para a quantidade.")
            return
        if quantidade_emprestada <= livros[titulo]["quantidade"]:
            livros[titulo]["quantidade"] -= quantidade_emprestada
            historico.append((titulo, quantidade_emprestada))
            print(f'Empréstimo de {quantidade_emprestada} exemplares do livro "{titulo}" registrado com sucesso!')
        else:
            print("Erro: Não há exemplares suficientes disponíveis.")
    else:
        print("Erro: Livro não encontrado.")

def exibir_historico(historico):
    if not historico:
        print("Nenhum empréstimo registrado.")
    else:
        print("Histórico de Empréstimos:")
        for titulo, quantidade in historico:
            print(f'Livro: "{titulo}", Quantidade emprestada: {quantidade}')

#As opções do menu são: Adicionar livro, Listar livros, Remover livro, Atualizar quantidade de livros, registrar empréstimo, Exibir histórico de empréstimos, Sair.
def main():
    while True:
        print(menu())
        opcao = input("Escolha uma opção (1-7): ").strip()
        if opcao == '1':
            add_livro(biblioteca_livros)
        elif opcao == '2':
            listar_livros(biblioteca_livros)
        elif opcao == '3':
            remover_livro(biblioteca_livros)
        elif opcao == '4':
            atualizar_quantidade(biblioteca_livros)
        elif opcao == '5':
            registrar_emprestimo(biblioteca_livros, historico_emprestimos)
        elif opcao == '6':
            exibir_historico(historico_emprestimos)
        elif opcao == '7':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

