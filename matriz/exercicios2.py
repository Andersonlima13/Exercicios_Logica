'''Escreva um programa que:
• Leia (ou gere aleatoriamente) uma matriz quadrada de ordem N contendo elementos
inteiros (N será lido);
• Exiba a matriz lida (no formato de matriz);
• Exiba os elementos da diagonal principal, isto é, os elementos onde I = J.'''

linhas = int(input("digite o numero de linhas e colunas : "))
colunas = linhas


principal = [[None]]
Matriz = [[None] * colunas for i in range(linhas)]


for i in range(linhas):
    for j in range(colunas):
        Matriz[i][j]  = int(input("digite um valor:  "))
       


for i in range(linhas):
    for j in range(colunas):
        if i == j:
            print(f'{Matriz[i][j]}')
          
