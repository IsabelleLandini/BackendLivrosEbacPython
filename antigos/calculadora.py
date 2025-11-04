print ("Escolha a operação:")
print("1-soma:")
print("2-subtração:")
print("3-multiplicação:")
print("4-divisão:")

opcao= input("Digite o número da operação desejada: ")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if opcao == '1':
    print("Resultado: ", num1 + num2)
elif opcao == '2':
    print("Resultado: ", num1 - num2)
elif opcao == '3':
    print("Resultado: ", num1 * num2)
elif opcao == '4':
    if num2 != 0:
        print("Resultado: ", num1 / num2)
    else:
        print("Erro: Divisão por zero não é permitida.")
else:
    print("Opção inválida. Por favor, escolha uma operação válida.")

opcao= input("Deseja realizar outra operação? (s/n): ")
if opcao.lower() == 's':
    print("Reiniciando a calculadora...")
else:       
    print("Obrigado por usar a calculadora!")
