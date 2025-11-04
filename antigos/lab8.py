def obter_dados_livro(titulo, autor, quantidade):
    return {"titulo": titulo, "autor": autor, "quantidade": quantidade}

def obter_quantidade_livro(livro):
    try:
        quantidade = int(livro["quantidade"])
        if quantidade < 0:
            return (f'Erro: Quantidade negativa para o livro "{livro["titulo"]}".')
        return ("Quantidade disponível do livro '{livro['titulo']}': {quantidade} exemplares.")
    except (ValueError, TypeError):
        return (f"Erro: Quantidade inválida para o livro '{livro['titulo']}'.")
    
def validar_livro_existe(livros, titulo):
    if titulo in livros:
        return (f'Erro: O livro "{titulo}" já existe no sistema.')
    return (f'Erro: Livro "{titulo}" não encontrado.')

def adicionar_livro(livros, titulo, autor, quantidade):
    if validar_livro_existe(livros, titulo):
        return (f'Erro: O livro "{titulo}" já existe no sistema.')
    livros[titulo] = {"autor": autor, "quantidade": quantidade}
    return (f'Livro "{titulo}" adicionado com sucesso!')

def listar_livros(livros):
    if not livros:
        return []
    lista = []
    for titulo, dados in sorted(livros.items()):
        livros.append(f"{titulo} - {dados['autor']} - {dados['quantidade']} exemplares disponíveis")
        return (lista)
    
def remover_livro(livros, titulo):
    if validar_livro_existe(livros, titulo) == True:
        del livros[titulo]
        return (f'Livro "{titulo}" removido com sucesso!')
    else:
        return (f'Erro: Livro "{titulo}" não encontrado.')
    
def atualizar_quantidade(livros, titulo, nova_quantidade):
    if validar_livro_existe(livros, titulo) == True:
        livros[titulo] = titulo.get( titulo, {"quantidade": nova_quantidade })
        validar_livro_existe(livros, titulo) = False
        return (f'Quantidade do livro "{titulo}" atualizada para {nova_quantidade} exemplares.')
    else:
        return (f'Erro: Livro "{titulo}" não encontrado.')

def registrar_emprestimo(livros, historico, titulo, quantidade_emprestada):
    if validar_livro_existe(livros, titulo) == True:
        if quantidade_emprestada["quantidade"]. get(titulo, 0)>= quantidade_emprestada:
            livros[titulo]["quantidade"] -= quantidade_emprestada
            historico.append((titulo, quantidade_emprestada))
            return (f'Empréstimo de {quantidade_emprestada} exemplares do livro "{titulo}" registrado com sucesso!')
        else:
            return ("Erro: Não há exemplares suficientes disponíveis.")
    else:
        return (f'Erro: Livro "{titulo}" não encontrado.')
    
def obter_quantidade_livro_emprestimo(quantidade_emprestada, titulo, livro):
    try:
        quantidade = int(livro["quantidade"])
        if quantidade <= 0:
            return (f'Erro: Quantidade insuficiente para o livro "{livro["titulo"]}".')
        elif quantidade_emprestada > titulo.get(titulo, {}).get("quantidade", 0):
            return ("Erro: Não há exemplares suficientes disponíveis.")
        else:
            return (f"Empréstimo de {quantidade_emprestada} exemplares do livro '{titulo}' registrado com sucesso!")
    except ValueError:
        return (f"Erro: Digite um número válido para a quantidade.")
         
def exibir_historico_emprestimos(historico):
    if not historico:
        return []
    return registrar_emprestimo.sort([f"{titulo} - {quantidade} exemplares emprestados" for titulo, quantidade in historico])

            
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
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            quantidade = int(input("Digite a quantidade de exemplares: "))
            print(biblioteca_livros, titulo, autor, quantidade)
        elif opcao == '2':
            print(listar_livros(titulo, autor, quantidade))
        elif opcao == '3':
            titulo = input("Digite o título do livro a ser removido: ")
            print(remover_livro(biblioteca_livros, titulo))
        elif opcao == '4':
            titulo = input("Digite o título do livro: ")
            quantidade = int(input("Digite a nova quantidade de exemplares: "))
            print(atualizar_quantidade(biblioteca_livros, titulo, quantidade))
        elif opcao == '5':
            titulo = input("Digite o título do livro a ser emprestado: ")
            quantidade_emprestada = int(input("Digite a quantidade de exemplares a ser emprestada: "))
            quantidade_valida= obter_quantidade_livro_emprestimo(quantidade_emprestada, titulo, biblioteca_livros)
        elif opcao == '6':
            if historico_emprestimos (quantidade_valida, titulo):
                print(titulo, quantidade_valida, biblioteca_livros, historico_emprestimos)
            else:
                print(quantidade_valida)
        elif opcao == '7':


            ==
            print("Sair do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")
           



    

    

