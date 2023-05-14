n = int(input("digite o numero da ordem da matriz:  "))

matriz = [[None] *n for i in range(n)]
matrizb = [[None]*n for i in range(n)] 

for linha in range(n):
    for coluna in range(n):
        matriz[linha][coluna] = int(input(f"digite um numero na posição i({linha}) j({coluna}):  "))  


for linha in range(n):
    for coluna in range(n):
        matrizb[linha][coluna] = matriz[linha][coluna]
        if linha == coluna or linha + coluna == n - 1:
            matrizb[linha][coluna] = 0
        else:
            matrizb[linha][coluna] = matrizb[linha][coluna] + linha + coluna
print(matrizb)