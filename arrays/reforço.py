''' PROCURE O MAIOR E MENOR VALOR DENTRO DE UM ARRAY '''


array = []
n = int(input("digite o tamanho do vetor"))

for i in range(n):
    valor = int(input(" digite um valor para adicionar ao vetor"))
    array = array + [valor]    
    maior = array[0]
    menor = array[0]
    
for i in range(n):
    if array[i] > maior:
        maior = array[i]
    if array[i] < menor:
        menor = array[i]
     
 


print(menor)
print(maior)
