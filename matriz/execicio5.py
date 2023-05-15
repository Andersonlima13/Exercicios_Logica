import random
linhas = 6
colunas = 3


notas = [[None] * (colunas+1) for i in range(linhas)]

for i in range(linhas):
    for j in range(colunas):
        notas[i][j] = random.randint(0,100)
       
for i in range(linhas):
    soma = 0
    for j in range(colunas):
        soma = soma + notas[i][j]
        notas[i][colunas] = round(soma/colunas)

soma = 0
for i in range(linhas):
    soma += notas[i][colunas]
media = round(soma/linhas)
print(f'\nMédia geral da turma: {media}')


print(notas)