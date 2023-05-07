'''Escreva um programa para ler 6 números. Após a leitura dos números, verifique,
para cada um deles, se é distinto, ou seja, não possui repetição.'''

n = 6

vetor = []
repetidos = []
for i in range(n):
    num = int(input("digite o valor a ser adcionado no vetor :  "))  
    vetor = vetor + [num]
if num in vetor == i:
    print("igua")
    

print(vetor)
