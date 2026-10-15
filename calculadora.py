nome = input("Matheus")
print(f"Bem vindo king {nome}")
numero1 = float(input("Imprima o primeiro numero"))

numero2 = float(input("Imprima o segundo numero: "))
if numero1 > numero2:
    print("O primeiro numero e maior que o segundo numero")
elif numero1 < numero2:
    print("O segundo numero e maior que o primeiro numero")
else:
    print("Os dois numeros sao iguais")

soma = numero1 + numero2
print(f"resultado da soma : {soma}")
multiplicao = numero1 * numero2
print(f"Resultado da multiplicacao : {multiplicao}")
subtracao = numero1 - numero2
print(f"Resultado da subtracao : {subtracao}")
