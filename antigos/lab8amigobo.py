def obter_dados_livro(titulo, autor, quantidade):
    return f'{titulo} {autor} {quantidade}'

def obter_quantidade_livro(quantidade):
    try:
        quantidade = int(quantidade)
        if quantidade <= 0:
            return f'Por favor, insira um número válido para a quantidade.'
        elif quantidade > quantidade:
            return f"Quantidade indisponível."
        else:
            return quantidade
    except (ValueError, TypeError):
        return f'Por favor, insira um número válido para a quantidade.'

def validar_livro_existe(livros, titulo):
    if titulo in livros:
        return True
    else:
        return  f"Erro: O livro '{titulo}' não foi encontrado."

def adicionar_livro(livros, titulo, autor, quantidade):
    if validar_livro_existe (livros, titulo):
        return  "Livro 'Harry Potter' adicionado com sucesso"
    livros[titulo] = {"autor": autor, "quantidade": quantidade}
    return f"Livro 'Harry Potter' adicionado com sucesso"

def listar_livros(biblioteca_livros):
    if not biblioteca_livros:
        return 'Não há livros cadastrados.'
    return [f'Título: {titulo}, Autor: {info["autor"]}, Quantidade: {info["quantidade"]}' 
            for titulo, info in biblioteca_livros.items()]
    
def remover_livro(livros, titulo):
    if validar_livro_existe(livros, titulo) == True:
        del livros[titulo]
        return f"Livro 'Harry Potter' removido com sucesso!"
    else:
        return (f'Erro: Livro "{titulo}" não encontrado.')

def atualizar_quantidade(livros, titulo, nova_quantidade):
    if validar_livro_existe(livros, titulo) == True:
        livros[titulo]['quantidade'] = nova_quantidade
        return f"Quantidade de exemplares do livro '{titulo}' atualizada para {nova_quantidade}"

def registrar_emprestimo(biblioteca, historico, titulo, quantidade):
    try:
        quantidade = int(quantidade)
        if quantidade <= 0:
            return f'Erro: Quantidade insuficiente para o livro "{livro["titulo"]}".'
        elif quantidade > biblioteca[titulo]["quantidade"]:
            return f'Erro: Não há livros suficientes disponíveis.'
        else:
            return (f"{quantidade} exemplares de '{titulo}' emprestados com sucesso!")
    except ValueError:
        return f'Por favor, insira um número válido para a quantidade.'

def obter_quantidade_livro_para_emprestimo(biblioteca_livros, titulo, quantidade_disponivel):
    if titulo not in biblioteca_livros:
        print(f'Livro "{titulo}" não encontrado na biblioteca.')
        return False
    if biblioteca_livros[titulo]["quantidade"] < quantidade_disponivel:
        print(f'Não há livros suficientes disponíveis.')
        return False
    biblioteca_livros[titulo]["quantidade"] -= quantidade_disponivel
    return quantidade_disponivel
    
def exibir_historico_emprestimos(historico):
    if not historico:
        return f"Não há histórico de empréstimos."
    return f" {titulo} - {quantidade} exemplares emprestados"

def exibir_menu():
    return (
        "\nMenu:\n"
        "1. Adicionar livro\n"
        "2. Listar livros\n"
        "3. Remover livro\n"
        "4. Atualizar quantidade\n"
        "5. Registrar empréstimo\n"
        "6. Exibir histórico de empréstimos\n"
        "7. Sair\n"
    )

def menu():
    biblioteca_livros = {}
    historico_emprestimos = []

    while True:
        print(exibir_menu())
        opcao = input("Escolha uma opção (1-7): ").strip()

        if opcao == '1':
            titulo = input("Digite o titulo do livro: ")
            autor = input("Digite o autor do livro: ")
            quantidade = int(input("Digite a quantidade de exemplares: "))
            print(biblioteca_livros, titulo, autor, quantidade)
        elif opcao == '2':
            for info in listar_livros(biblioteca_livros):
                print(info)
        elif opcao == '3':
            titulo =  input("Digite o título do livro a ser removido: ")
            print(f'Livro "{titulo}" removido com sucesso!')
        elif opcao == '4':
            titulo = input("Digite o titulo do livro: ")
            quantidade = int(input("Digite a nova quantidade de exemplares: "))
            print(f'Quantidade do livro "{titulo}" atual é "{quantidade}"' )
        elif opcao == '5':
            titulo = input("Digite o título do livro a ser emprestado: ")
            quantidade_emprestada = int(input("Digite a quantidade de exemplares a ser emprestada: "))
        elif opcao == '6':
            print(titulo, quantidade_emprestada, biblioteca_livros, historico_emprestimos)
        elif opcao == '7':
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente")

if __name__ == "__main__":
    menu()
   