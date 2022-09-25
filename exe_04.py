"""
Criar um algoritmo que receba o salário de um funcionário
e informe a ele o valor descontado para o INSS e seu salário líquido!
"""

salario = float(input("Digite seu salário: "))

INSS = salario * 0.075

print(f"O desconto para o INSS foi de R$ {INSS}.")
