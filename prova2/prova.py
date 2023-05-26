''' CRIE UM PROGRAMA QUE LEIA UM VETOR DE 30 INTEIROS DE NUMEROS POSITIVOS E NEGATIVOS'''

vetor = []
n = 8


for i in range(n):
    valor = int(input("digite um numero para o vetor :  "))
    vetor = vetor + [valor]
    
soma_positivos = 0
count_positivos = 0
media_positivos = 0

for i in(vetor):
    if i > 0:
        soma_positivos = soma_positivos + i
        count_positivos = count_positivos +1
        media_positivos = soma_positivos / count_positivos
        
soma_negativos = 0
count_negativos = 0
media_negativos = 0
        
for i in(vetor):
    if i < 0:
        soma_negativos = soma_negativos + i
        count_negativos = count_negativos +1
        media_negativos = soma_negativos / count_negativos
        
    

print(f" a media dos numeros positivos é de {media_positivos}")
print(f" a media dos numeros negativos é de {media_negativos}")

