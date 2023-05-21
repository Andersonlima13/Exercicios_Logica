'''Uma matriz de permutação é uma matriz quadrada cujos elementos são 0's
ou 1's, tal que em cada linha e em cada coluna exista apenas um elemento
igual a 1. Por exemplo, a matriz seguinte é uma matriz de permutação.
1 0 0
0 1 0
0 0 1
Com base na definição apresentada, escreva um programa que preencha uma
matriz quadrada com valores fornecidos pelo usuário, determine e mostre se
ela é uma matriz de permutação.'''
# Testando as linhas


n = int(input('Digite a ordem da matriz: '))

# Criação da matriz com valores nulos
matriz = [[None]*n for i in range(n)]

# Leitura dos elementos da matriz
print('\nDigite os elementos da matriz (0 ou 1):')
for i in range(n):
    for j in range(n):
        matriz[i][j] = int(input(f'digite um valor para I[{i}] e J[{j}]: '))

# Exibição da matriz 
print('\nMatriz:')
for i in range(n):
    for j in range(n):
        print(f'{matriz[i][j]:4}',end='')
    print()

# Testando as linhas
teste_lin = True
for i in range(n):
    cont = 0
    for j in range(n):
        if matriz[i][j] == 1:
            cont += 1
    if cont != 1:
        teste_lin = False
        break

# Testando as colunas
teste_col = True
for j in range(n):
    cont = 0
    for i in range(n):
        if matriz[i][j] == 1:
            cont += 1
    if cont != 1:
        teste_col = False
        break

if teste_lin and teste_col:
    print('\nÉ uma matriz de permutação')
else:
    print('\nNão é uma matriz de permutação') 