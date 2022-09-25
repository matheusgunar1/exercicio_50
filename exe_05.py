"""
Crie um algoritmo que receba dois valores
e que pergunte ao usuário qual tipo de cálculo deseja que seja feito (soma, subtração, multiplicação ou divisão).
E que dê ao usuário a capacidade de indicar qual operação deseja.
"""
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

operacao = input("Escolha a operação desejada: "
                 "A - soma,  "
                 "B - subtração, "
                 "C - multiplicação, "
                 "D - divisão"
                 ":  ")
if operacao == "A":
    calculo = valor1 + valor2
    print(calculo)
elif operacao == "B":
    calculo = valor1 - valor2
    print(calculo)
elif operacao == "C":
    calculo = valor1 * valor2
    print(calculo)
else:
    calculo = valor1/valor2
    print(calculo)