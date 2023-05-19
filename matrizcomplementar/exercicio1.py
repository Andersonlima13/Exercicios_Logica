'''Uma matriz de permutação é uma matriz quadrada cujos elementos são 0's
ou 1's, tal que em cada linha e em cada coluna exista apenas um elemento
igual a 1. Por exemplo, a matriz seguinte é uma matriz de permutação.
1 0 0
0 1 0
0 0 1
Com base na definição apresentada, escreva um programa que preencha uma
matriz quadrada com valores fornecidos pelo usuário, determine e mostre se
ela é uma matriz de permutação.'''


valor = int(input("digite o valor para linhas e colunas"))

matriz = [[None]* valor for i in range(valor) ]

for i in range(valor):
    for j in range(valor):
        matriz[i][j] = int(input(f"digite o valor para o elemento i[{i}] e j[{j}]"))

print(matriz)