'''Escreva um programa que leia 10 números e armazene-os em um vetor. Exiba:
• Os números que estão nos índices pares;
• Os números que estão nos índices ímpares.'''

v = []
par = []
impar = []

for i in range(10):
  valor = int(input(f"digite um valor para a posição {i} :  "))
  v = v + [valor]
  if i % 2 == 0:
    par = i
    print(f"o valor {valor} está em um indice par")
  else:
    impar = i
    print(f" o valor {valor} está em um indice impar")
