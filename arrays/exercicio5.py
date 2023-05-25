'''Escreva um programa que receba um vetor V de N números inteiros (N será lido),
determine e exiba o maior e o menor elemento deste vetor e seus respectivos
índices.
Obs: suponha a inexistência de valores repetidos.'''

n = int(input("Digite o tamanho do vetor: "))
vetor = []

for i in range(n):
    num = int(input(f"Digite o elemento {i+1} do vetor: "))
    vetor = vetor + [num]

    maiorValor = vetor[0]
    indice_maiorValor = 0
    menorValor = vetor[0]
    indice_menorValor = 0

for i in range(n):
    if vetor[i] > maiorValor:
        maiorValor = vetor[i]
        indice_maiorValor = i
    if vetor[i] < menorValor:
        menorValor = vetor[i]
        indice_menorValor = i

print(f"O maiorValor elemento do vetor é {maiorValor} e está na posição {indice_maiorValor}.")
print(f"O menorValor elemento do vetor é {menorValor} e está na posição {indice_menorValor}.")
        
        

    
    