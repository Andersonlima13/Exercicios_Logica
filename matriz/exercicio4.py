import random

x = 3  # número de linhas da matriz M 
y = 5  # número de colunas da matriz M

# Criação das matrizes
m = [[None]*y for i in range(x)]
t = [[None]*x for i in range(y)]

# Leitura da matriz M
print('Digite os elementos da Matriz M:')
for i in range(x):
    for j in range(y):
        m[i][j] = random.randint(1,30)

# Geração da matriz T (transposta)
for i in range(x):
    for j in range(y):
        t[j][i] = m[i][j]

# Impressão da matriz M
print('\nMatriz M:')
for i in range(x):
    for j in range(y):
        print(f'{m[i][j]:4}',end='')
    print()
      
# Impressão da matriz T
print('\nMatriz T (transposta):')
for i in range(y):
    for j in range(x):
        print(f'{t[i][j]:4}',end='')
    print()
