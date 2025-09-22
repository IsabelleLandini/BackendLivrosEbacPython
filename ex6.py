# calculadora simples
#define o menu de opções

menu = ["1- soma", "2- subtração", "3- multiplicação", "4- divisão", "5-Sair"]
menu_simples = [item for item in menu if item != "5-Sair"]

# Define as operações usando funções lambda
soma = lambda x, y: x + y
subtracao = lambda x, y: x - y
multiplicacao = lambda x, y: x * y
divisao = lambda x, y: x / y 

# Solicita os números ao usuário
def adicionar_numero():
    try:
        x = float(input("Digite o primeiro número: "))
        y = float(input("Digite o segundo número: "))
        return x, y
    except ValueError:
        print("Erro: Entrada inválida. Por favor, insira números válidos.")
        return adicionar_numero()


def main():
    while True:
        print("\n" + '\n'.join(menu_simples))
        opcao = input("Escolha uma opção (1-5): ").strip()
        if opcao == '1':
            x, y = adicionar_numero()
            print(f"Resultado da soma: {soma(x, y)}")
            input("Deseja realizar outra operação? S/N")
        elif opcao == '2':
            x, y = adicionar_numero()
            print(f"Resultado da subtração: {subtracao(x, y)}")
            input("Deseja realizar outra operação? S/N")
        elif opcao == '3':
            x, y = adicionar_numero()
            print(f"Resultado da multiplicação: {multiplicacao(x, y)}")
            input("Deseja realizar outra operação? S/N")
        elif opcao == '4':
            x, y = adicionar_numero()
            while y == 0:
                print("Erro: Divisão por zero não é permitida.")
                y = float(input("Digite novamente o segundo número: "))
            print(f"Resultado da divisão: {divisao(x, y)}")
            input("Deseja realizar outra operação? S/N")
        elif opcao == '5':
            print("Sair do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

 