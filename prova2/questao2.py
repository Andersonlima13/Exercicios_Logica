# Lendo a 
import random
matriz = []
for i in range(10):
    linha = []
    for j in range(12):
        valor = random.randint(10,100)
        linha.append(valor)
    matriz.append(linha)

# Listando a soma dos números da primeira linha
primeira_linha = matriz[0]
soma_primeira_linha = sum(primeira_linha)
print("Soma dos números da primeira linha:", soma_primeira_linha)

# Calculando a média da última coluna
ultima_coluna = [linha[-1] for linha in matriz]
media = sum(ultima_coluna) / len(ultima_coluna)
print("Média da última coluna:", media)

# Exibindo a matriz completa
print("\nMatriz completa:")
for linha in matriz:
    for valor in linha:
        print(valor, end="\t")
    print()
