'''Escreva um programa para ler 6 números. Após a leitura dos números, verifique,
para cada um deles, se é distinto, ou seja, não possui repetição.'''

import random

n = 6
vetor = [None]*n
for i in range(n):
    vetor[i] = random.randint(1,10)
print(vetor)
for j in vetor:
    if vetor.count(j) > 1:
        print(j,'repete')
    else:
        print(j,'não repete')
        