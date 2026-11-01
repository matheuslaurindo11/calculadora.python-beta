while True:
    opcao = input(
        "Escolha uma opcao:"
        "n1 - Soma \n"
        "n2 - Subtracao \n"
        "n3 - Multiplicacao \n"
        "n4 - Divisao \n"
        "n5 - Sair \n"

    ) .strip()

    if opcao == "5":
        print("Saindo da calculadora")

        break
    numero1 = float(input("Imprima o primeiro numero:"))
    numero2 = float(input("Imprima o segundo numero:"))
    if opcao == "1":
        soma = numero1 + numero2
        resultado = "Voce Escolheu a Opcao De Soma"
        print(f"Resultado Da Soma: {soma}")
    elif opcao == "2":
        resultado = "Voce escolheu a opcao de subtracao"
        subtracao = numero1 - numero2
        print(f"Resultado da subtracao: {subtracao}")
    elif opcao == "3":
        resultado = "Voce Escolheu a Opcao De Multiplicacao"
        multiplicacao = numero1 * numero2
        print(f"Resultado Da Multiplicacao: {multiplicacao}")
    elif opcao == "4":
        resultado = "Voce escolheu a opcao de divisao"
        print(f"Resultado da Divisao: {divisao}")
        if numero2 == 0:
            print("Erro: Divisao por zero nao e permitida.")
        else:
            divisao = numero1 / numero2
            print(f"Resultado Da Divisao: {divisao}")
