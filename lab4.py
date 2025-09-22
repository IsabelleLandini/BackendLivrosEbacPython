#criar um programa para gerenciar o estoque

estoque={}

def menu():
    return(
        """Menu:\n
        1 - Adicionar produto \n
        2 - Listar produtos \n
        3 - Remover produto \n
        4 - Atualizar quantidade do produto \n
        5 - Sair do programa"""
    )

def adicionar_produto(nome):
    nome = nome.strip("Digite o nome do produto: ")
    if nome in estoque:
        return "Esse produto já existe."
    else:
        quantidade = int(input("Digite a quantidade do produto: "))
        preço = float(input("Digite o preço do produto: "))
        if quantidade < 0 or preço < 0:
            return "Erro: Quantidade e preço devem ser valores positivos."
        else:
            estoque[nome] = {'quantidade': quantidade, 'preço': preço}
            return f"Produto '{nome}' com quantidade {quantidade} e preço {preço} adicionado com sucesso!"
        

def valor_produto(quantidade, preço):
    nome= input.strip("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade do produto: "))
    preço = float(input("Digite o preço do produto: "))
    if quantidade < 0 or preço < 0:
        return "Erro: Quantidade e preço devem ser valores positivos."
    else:
        estoque[nome] = {'quantidade': quantidade, 'preço': preço}
        return f"Produto '{nome}' com quantidade {quantidade} e preço {preço} adicionado com sucesso!"


def listar_produtos(estoque):
    if not estoque:
        return "Nenhum produto cadastrado."
    else:
        resultado = ["Lista de produtos"]
        for nome, info in sorted(estoque.items(), key=lambda item: item[0]):
            quantidade = info['quantidade']
            preço = info['preço']
            resultado.append(f"{nome}: Quantidade: {quantidade}, Preço: {preço}")
        return "\n".join(resultado)
    
def remover_produto(nome):
    nome= nome.strip("Digite o nome do produto: ")
    if nome in estoque:
        del estoque[nome]
        return (f"Produto '{nome}' removido com sucesso!")
    else:
        return ("Erro: Produto não encontrado.")
    
def atualizar_quantidade(nome, nova_quantidade):
    nome = nome.strip("Digite o nome do produto: ")
    if nome in estoque:
        nova_quantidade = int(input("Digite a nova quantidade do produto: "))
        if nova_quantidade < 0:
            return "Erro: Quantidade deve ser um valor positivo."
        else:
            estoque[nome]['quantidade'] = nova_quantidade
            return f"Quantidade do produto '{nome}' atualizada para {nova_quantidade} com sucesso!"
    else:
        return ("Erro: Produto não encontrado.")
    
def main():
    while True:
        print(menu())
        opcao = input("Escolha uma opção (1-5): ").strip()
        if opcao == '1':
            nome = input("Adicionar produto: ")
            print(adicionar_produto(nome))
        elif opcao == '2':
            print(listar_produtos(estoque))
        elif opcao == '3':
            nome = input("Remover produto: ")
            print(remover_produto(nome))
        elif opcao == '4':
            nome = input("Atualizar quantidade do produto: ")
            print(atualizar_quantidade(nome, nova_quantidade=None))
        elif opcao == '5':
            print("Sair do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()