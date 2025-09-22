# Lista de convidados VIP (pode ser modificada nos testes)
convidados_vip = ["Alice", "Bob", "Carol"]

# Função para verificar se a idade permite entrada
def verificar_idade(idade):
    if idade >= 18:
        return ("Entrada permitida. Bem-vindo ao evento!")
    else:
        return ("Entrada negada. Este evento é apenas para maiores de  idade.")

# Função para verificar se o nome está na lista VIP
def verificar_vip(nome):
    if nome in convidados_vip:
        return ("Você é um convidado VIP! Aproveite o evento com acesso especial.")
    else: 
        return None
    
    # Programa principal
def main():
    print("Bem-vindo ao evento!")


    idade_input= input("Digite sua idade: ")

    if not idade_input.isdigit () == True:
        print("Erro: Por favor, insira um número válido para a idade.")
        return

    try:
        idade = int(idade_input)
    except ValueError:
        print("Erro: Por favor, insira um número válido para a idade.")
        return
    messagem= verificar_idade(idade)
    print(messagem)
    
    if idade >= 18:
        nome=input("Digite seu nome: ")
        if not nome.isalpha()== True:
            print("Erro: Por favor, insira um nome válido (apenas letras).")
            
            mensagem_vip = verificar_vip(nome)  
            if mensagem_vip:
                print(mensagem_vip)
            else:
                print("Você não está na lista VIP. Aproveite o evento!")
        
if __name__ == "__main__":
    main()

    
