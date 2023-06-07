'''Escreva um programa que leia N números inteiros (máximo 20) e armazene em um vetor X.      

Calcule a média dos elementos do vetor e informe quantos elementos estão abaixo da média do conjunto.       

Crie as seguintes funções:

*	Uma função que faça a leitura dos elementos de um vetor.

*	Uma função que retorne a média dos elementos de um vetor.

*	Uma função que receba um vetor e um número, e retorne quantos elementos do vetor estão abaixo desse número. 
'''


#Função para ler um vetor
def leitura(v):
    for i in range(len(v)):
        v[i] = int(input())  

#Função para calcular a média de um vetor
def media(v):
    soma = 0
    for i in range(len(v)):
        soma += v[i]
    return soma/len(v)

#Função para contar os elementos abaixo da média
def contagem(v,n):
    cont = 0
    for i in range(len(v)):
        if v[i] < n:
            cont += 1
    return cont

#Programa principal
qtd = 5  #Testando com apenas 5 elementos
x = [None]*qtd
print(f'Digite {qtd} números inteiros:')
leitura(x)
m = media(x)
c = contagem(x,m)
print(f'A média do elementos do vetor é: {m:.1f}')
print(f'Existe(m) {c} elemento(s) abaixo da média')
