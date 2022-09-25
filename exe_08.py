"""
Crie um programa que calcule uma e imprima uma tabuada de acordo com a escolha do clinte.
"""
print("---------------------------------------------------------------------------------------------------------------")
print("Este programa imprime a tabuada de 1 a 10 para um número de escolha do usuário!")
print("---------------------------------------------------------------------------------------------------------------")

resp = "S"
i = 1
valor = int(input("Digite o valor desejado:  "))

while i <= 10:
        calculo = valor * i
        print(f" {valor} x {i} = {calculo}")
        i += 1
print("Obrigado!")
print("---------------------------------------------------------------------------------------------------------------")


