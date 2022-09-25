"""
Crie um programa que converta valores de Celsius para Farenheit.
"""
print("Este é um progrma para conversão de valores entre as escalas Celsius e Farenheit!")
print("-----------------------------------------------------------------------")
escala = input("Escolha a escala termométrica do valor a ser inserido (C - Celsius e F - Farenheit):  ")
valor = int(input("Digite o valor a ser convertido:  "))

if escala == "C":
    F1 = float(((valor/5)*9)+32)
    print(f"O valor digitado corresponde em graus Farenheit a {F1} °F.")
elif escala == "F":
    C1 = float(((valor-32)/9)*5)
    print(f"O valor digitado corresponde em graus Celsius a {C1} °C.")
print("------------------------------------------------------------------------")
