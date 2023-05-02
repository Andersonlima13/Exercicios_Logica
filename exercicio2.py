Tamanho = 10
V = []
K = int(input("digite o valor a ser buscado dentro do vetor:  "))
cont = 0


for i in range(Tamanho):
   Elemento = int(input("digite um numero inteiro:  "))
   V = V + [Elemento]
for i in(V):
    if i == K:
        cont += 1

print(f" o elemento {K} apareceu {cont} vezes")


