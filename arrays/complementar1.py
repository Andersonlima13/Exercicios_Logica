'''Escreva um programa que leia um vetor contendo N elementos inteiros (N será
lido), calcule e exiba:
• A quantidade de elementos pares;
• A quantidade de elementos ímpares;
• A soma de todos os elementos;
• A média dos elementos do vetor.'''


n = int(input("Digite o tamanho do vetor: "))
vetor = []
impar = 0
par = 0
soma = 0

for i in range(n):
    num = int(input(f"Digite o elemento {i+1} do vetor: "))
    vetor = vetor + [num]
    
    
for i in(vetor):
    soma = soma + i
    media = soma / n
    if i % 2 == 0:
        par = par + 1
    else:
        impar = impar + 1

print(f" a média de todos os valores é {media}")
print(f" a soma de todos os valores é {soma}")
print(f" o vetor contém {par} elementos pares")
print(f" o vetor contém {impar} elementos impares")