def encontrar_maior_valor(vetor):
    if len(vetor) == 0:
        print("O vetor está vazio.")
        return None

    maior = vetor[0]
    for elemento in vetor:
        if elemento > maior:
            maior = elemento

    return maior

# Exemplo de uso
vetor = []

# Leitura do vetor
n = int(input("Digite o tamanho do vetor: "))
for i in range(n):
    valor = int(input("Digite o valor para a posição {}: ".format(i)))
    vetor.append(valor)

# Chamada da função para encontrar o maior valor
maior_valor = encontrar_maior_valor(vetor)

# Impressão do resultado
if maior_valor is not None:
    print("O maior valor do vetor é:", maior_valor)