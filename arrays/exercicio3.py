'''3. Escreva um programa que leia um vetor V contendo N elementos inteiros (N será
lido) e um valor inteiro K, verifique e exiba se o K está ou não no vetor. Se estiver,
informe em que posição (índice).
Obs: K pode se repetir no vetor, nesse caso, mostre todas as posições onde o K
aparece.'''


Tamanho = int(input("digite o tamanho do vetor :  "))

v = []
k = int(input("digite o valor a ser buscador dentro do vetor:  "))


for i in range(Tamanho):
  valor = int(input(f"digite um valor para a posição {i} :  "))
  v = v + [valor]
  if v[i] == k:
    print(f"elemento {valor} na posição {i}")
