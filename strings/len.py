"""Faça um programa que leia o nome de uma pessoa e exiba-o conforme o exemplo abaixo.    
Obs: Suponha que o nome lido não possua nenhuma preposição, artigo, etc.     

Exemplo:     
* Entrada: 
> FLAVIO RIBEIRO COUTINHO 
* Saída: 
> COUTINHO, F. R."""


nome = input('Nome:\n').upper()


parte = nome.split()
n = len(parte)
print(n)
saida = parte[n-1] + ', '

for i in range(n-1):
    saida = saida + parte[i][0] + '. '

print('\nNome formatado:')
print(saida)
