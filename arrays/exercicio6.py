'''Escreva um programa que leia um vetor de N números inteiros (N será lido),
inverta a ordem dos elementos do vetor e exiba o vetor invertido.
Ex: V = [1, 3, 5, 7], após a inversão: V = [7, 5, 3, 1].
Obs: É necessário inverter os elementos do vetor, não basta imprimi-los em
ordem inversa!'''


n = int(input("Digite o tamanho do vetor: "))
vetor = []

for i in range(n):
    num = int(input(f"Digite o elemento {i+1} do vetor: "))
    vetor = vetor + [num]
    
for i in range(n//2):
    aux = vetor[i]
    vetor[i] = vetor[n-i-1]
    vetor[n-i-1] = aux

print(vetor)