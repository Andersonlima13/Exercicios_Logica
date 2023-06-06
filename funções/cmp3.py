#Versão usando find

s = input('Digite uma frase:\n')
n = int(input('\nDigite um valor inteiro:\n'))

vogais = 'AaEeIiOoUu'
saida = ''

for caracter in s:
    if vogais.find(caracter) >= 0:
        saida = saida + caracter * n    
    else:
        saida = saida + caracter 

print(f'\nSaída:\n{saida}')
