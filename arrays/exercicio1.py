'''Escreva um programa que leia um vetor A de N números inteiros (N será lido) e
um outro inteiro K, construa e exiba um outro vetor B cujos elementos são os
respectivos elementos de A multiplicados por K.'''


N = int(input("Digite o tamanho do vetor: "))
A = []

for i in range(N):
    num = int(input("Digite um valor inteiro: "))
    A = A + [num]

K = int(input("Digite um número inteiro para multiplicar os valores do vetor: "))
B = []

for i in range(N):
    B = B + [A[i] * K]

print("Vetor B:", B)