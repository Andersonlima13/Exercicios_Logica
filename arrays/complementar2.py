'''1. Escreva um programa que leia um vetor contendo N elementos inteiros (N será
lido), calcule e exiba:
• A quantidade de elementos pares;
• A quantidade de elementos ímpares;
• A soma de todos os elementos;
• A média dos elementos do vetor.'''


n = int(input("digite o tamanho dos vetores:  "))

vetorA = []
vetorB = []
vetorC = []

for i in range(n):
    num = int(input("digite o elemento a ser adcionado no vetor A:  "))
    vetorA = vetorA + [num]
for i in range(n):
    num = int(input("digite o elemento a ser adcionado no vetor B:  "))
    vetorB = vetorB + [num]

    
for i in(vetorA):
    vetorC = vetorC + [i]
    
for i in(vetorB):
    vetorC = vetorC + [i]

print(vetorC)