n = 3

matriz = [[None] * n for i in range(n)]
 
for i in range(n):
    for j in range(n):
        matriz[i][j] = int(input(f"digite um valor para o elemento I[{i}] e J[{j}]"))


# SOMA DE TODAS AS LINHAS 
print('\nSOMA DAS linhas:')
for i in range(n):
    soma_linhas = 0
    for j in range(n):
        soma_linhas = soma_linhas + matriz[i][j]
    print(f'{soma_linhas:4}')



## SOMA DE TODAS AS COLUNAS
print('\nSOMA DAS COLUNAS:')

for j in range(n):
    soma_colunas = 0
    for i in range(n):
        soma_colunas = soma_colunas + matriz[i][j]
    print(soma_colunas)
    

## SOMA DAS DIAGONAL PRINCIPAL
print('\nDIAGONAL PRINCIPAL:') 
soma_diagonal = 0
for i in range(n):
    for j in range(n):
        if i == j:
            soma_diagonal = soma_diagonal + matriz[i][j]
print(soma_diagonal)
            
 
print('\nDIAGONAL SECUNDARIA:') 
            
soma_secundaria = 0
for i in range(n):
    for j in range(n):
        if i + j == n - 1:
            soma_secundaria = soma_secundaria + matriz[i][j]           

print(soma_secundaria)

print('\nVALOR TOTAL :')

soma_tudo = 0
for i in range(n):
    for j in range(n):
        soma_tudo = soma_tudo + matriz[i][j]

print(soma_tudo)


# PRINT DA MATRIZ

print('\nMatriz:')
for i in range(n):
    for j in range(n):
        print(f'{matriz[i][j]:4}',end='')
    print()
        
