import random

linhas = 10
colunas = 12
soma_linhas = 0

matriz = [[None]* colunas for i in range(linhas)]

for i in range(linhas):
    for j in range(colunas):
        matriz[i][j] = random.randint(10,100)


print('\nMatriz')
for i in range(linhas):
    for j in range(colunas):
        print(f'{matriz[i][j]:4}',end='')
    print()




for i in range(linhas-9):
    soma_linhas = soma_linhas + i
print(soma_linhas)

    

    