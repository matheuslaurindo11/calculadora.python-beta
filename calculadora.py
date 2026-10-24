opcao = input("Escolha uma opcao: \n1 - Soma, \n2 - Subtracao, \n3 - Multiplicacao, \n4 - Divisao")
nome = input("Qual e seu nome ? ")
print(f"Bem vindo {nome}")
numero1 = float(input("Imprima o primeiro numero"))
numero2 = float(input("Imprima o segundo numero: "))

if opcao == "1":
    resultado = "Voce escolheu a opcao de soma"

    print(resultado)
    soma = numero1 + numero2
    print(f"Resultado Da Soma : {soma}")

elif opcao == "2":
    resultado = "Voce escolheu a opcao de subtracao"
    print(resultado)
    subtracao = numero1 - numero2
    print(f"resultado da subtracao: {subtracao}")

elif opcao == "3":
    resultado = "Voce escolheu a opcao de multiplicacao"
    print(resultado)
    multiplicacao = numero1 * numero2
    print(f"resultado da multiplicacao: {multiplicacao}")

elif opcao == "4":
    resultado = "Voce escolheu a opcao de divisao"
    print(resultado)
    print(f"debug: numero2 = {numero2}")
elif opcao == "5":
    print("Saindo da calculadora")

else:
    divisao = numero1 / numero2
    print(f"resultado da divisao: {divisao}")
while True:
    opcao = input(
        "Escolha uma opcao:"
        "n1 - soma\n,"
        "n2 - subtracao\n,"
        "n3 - multiplicacao\n,"
        "n4 - divisao\n,"
        "n5 - sair\n"

    )

    if opcao == "5":
        print("Saindo da calculadora")

        break
    numero1 = float(input("Imprima o primeiro numero:"))
    numero2 = float(input("Imprima o segundo numero:"))
    if opcao == "1":
        soma = numero1 + numero2
        print(f"resultado da soma: {soma}")
    elif opcao == "2":
        subtracao = numero1 - numero2
        print(f"resultado da subtracao: {subtracao}")
    elif opcao == "3":
        multiplicacao = numero1 * numero2
        print(f"resultado da multiplicacao: {multiplicacao}")
    elif opcao == "4":
        if numero2 == 0:
            print("Erro: Divisao por zero nao e permitida.")
        else:
            divisao = numero1 / numero2
            print(f"resultado da divisao: {divisao}")
