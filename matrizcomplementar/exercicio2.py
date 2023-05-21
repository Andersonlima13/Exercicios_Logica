# Obtém a ordem da matriz do usuário
ordem = int(input("Digite a ordem da matriz quadrada: "))

# Inicializa a matriz
matriz = []
for i in range(ordem):
    linha = []
    for j in range(ordem):
        elemento = int(input(f"Digite o valor para a posição [{i}][{j}]: "))
        linha.append(elemento)
    matriz.append(linha)

# Calcula a soma de referência
soma_referencia = 0
for j in range(ordem):
    soma_referencia += matriz[0][j]

# Verifica a soma das linhas
quadrado_magico = True
for i in range(ordem):
    soma_linha = 0
    for j in range(ordem):
        soma_linha += matriz[i][j]
    if soma_linha != soma_referencia:
        quadrado_magico = False
        break

# Verifica a soma das colunas
if quadrado_magico:
    for j in range(ordem):
        soma_coluna = 0
        for i in range(ordem):
            soma_coluna += matriz[i][j]
        if soma_coluna != soma_referencia:
            quadrado_magico = False
            break

# Verifica a soma da diagonal principal
if quadrado_magico:
    soma_diagonal_principal = 0
    for i in range(ordem):
        soma_diagonal_principal += matriz[i][i]
    if soma_diagonal_principal != soma_referencia:
        quadrado_magico = False

# Verifica a soma da diagonal secundária
if quadrado_magico:
    soma_diagonal_secundaria = 0
    for i in range(ordem):
        soma_diagonal_secundaria += matriz[i][ordem - i - 1]
    if soma_diagonal_secundaria != soma_referencia:
        quadrado_magico = False

# Exibe o resultado
if quadrado_magico:
    print("A matriz é um quadrado mágico.")
else:
    print("A matriz não é um quadrado mágico.")