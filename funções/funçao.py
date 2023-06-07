#Função soma
def soma(vetor):
    somador = 0
    for i in range(len(vetor)):
        somador += vetor[i]
    return somador

#Programa principal
vetor = [6,3,8,7,2,5]
s = soma(vetor)
print(f'A soma dos valores é: {s}')