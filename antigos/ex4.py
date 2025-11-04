#criar um programa para gerenciar o estoque

estoque={}

def adicionar_produto(nome, quantidade, preço, estoque):
    adicionar_produto = nome.strip()   
    if nome in estoque:
        return "Erro: Produto já cadastrado."
    else:
        estoque[nome] = {'nome', 'quantidade', 'preço'}
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
    
    
def remover_produto(nome, estoque):
    nome= nome.strip()
    if nome in estoque:
        del estoque[nome]
        return f"Produto '{nome}' removido com sucesso!"
    else:
        return "Erro: Produto não encontrado."
    

def atualizar_quantidade(nome, nova_quantidade, estoque):
    nome = nome.strip()
    if nome in estoque:
        estoque[nome] = {'quantidade': nova_quantidade}
        return f"Quantidade do produto '{nome}' atualizada para {nova_quantidade} com sucesso!"
    else:
        return ("Erro: Produto não encontrado.")
    

def exibir_menu():
    return(
        """Menu:\n
        1 - Adicionar produto \n
        2 - Listar produtos \n
        3 - Remover produto \n
        4 - Atualizar quantidade do produto \n
        5 - Sair"""
    )


def main():
    while True:
        print(exibir_menu())
        opcao = input("Escolha uma opção (1-5): ").strip()
        if opcao == '0':
            nome = input("Digite o nome do produto: ")
            quantidade= int(input("Digite a quantidade do produto: "))
            preço= float(input("Digite o preço do produto: "))
            print(adicionar_produto(nome, quantidade, preço, estoque))
            
        elif opcao == '1':
            nome = input("Adicionar produto: ")
            print(adicionar_produto(nome))
        elif opcao == '2':
            nome= input("Listar produtos: ")
            print(listar_produtos(nome, estoque))
        elif opcao == '3':
            nome = input("Remover produto: ")
            nova_quantidade= int(input("Digite a nova quantidade do produto: "))
            print(remover_produto(nome, quantidade, estoque))
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


    


    
    



