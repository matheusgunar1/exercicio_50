"""
Crie um programa que receba o nome de um aluno e três notas, trabalho com peso 4, teste com peso 3 e prova com peso 5.
Em seguida deve calcular e imprimir a média ponderada.
"""
nome = input("Digite o nome do aluno:   ")
notas = [float(input("Digite a nota do trabalho: ")),float(input("Digite a nota do teste: ")),
         float(input("Digite a nota da prova: "))]
print(notas)

media = (notas[0]*4+notas[1]*3+notas[2]*5)/12

print(f"O aluno {nome} ficou com média igual a {media}!")