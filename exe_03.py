"""
Crie um programa que receba um nome e três notas e depois calcule a média final. Se a média for maior que 7
o programa deve imprimir aprovado, senão imprimir reprovado.
"""
nome = input("Digite seu nome: ")
nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
nota3 = float(input("Digite sua terceira nota: "))

print("-----------------------------------------------------------------------")

media = (nota1 + nota2 +nota3)/3

if media > 7:
    print("Aprovado!!!")
else:
    print("Reprovado!!!")
print("------------------------------------------------------------------------")