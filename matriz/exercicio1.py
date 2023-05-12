'''Escreva um programa que preencha duas matrizes (A e B), ambas de ordem 2x3, com
valores inteiros fornecidos pelo usuário (ou gerados aleatoriamente). O programa
deverá somar as duas matrizes, armazenando o resultado em uma terceira matriz (C).
Ao final, exiba as 3 matrizes (no formato de matriz).'''
linhas = 2  # número de linhas da matriz
colunas = 3  # número de colunasunas da matriz

# Criação das matrizes
a = [[None]*colunas for i in range(linhas)]
b = [[None]*colunas for i in range(linhas)]
c = [[None]*colunas for i in range(linhas)]

# Leitura da matriz A
print('Digite os elementos da Matriz A:')
for i in range(linhas):
    for j in range(colunas):
        a[i][j] = int(input(f'A[{i}][{j}]: '))

print('Digite os elementos da Matriz B:')
for i in range(linhas):
    for j in range(colunas):
        b[i][j] = int(input(f'B[{i}][{j}]: '))
        
for i in range(linhas):
    for j in range(colunas):
        c[i][j] = a[i][j] + b[i][j]
        
print(a)
print(b)
print(c)