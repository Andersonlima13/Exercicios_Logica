frase = input('Frase: ')
n = frase.count(' ')
print(f'A frase contém {n} brancos')

## elimina os espaços brancos

frase = input('Frase: ')
saida = frase.replace(' ','')
print(saida)

# replace => troca os elementos 

frase = input('Frase: ')
saida = frase.upper()
print(saida)

# deixa maiusculo



frase = input('Frase: ')
saida = frase.title()
print(saida)

#apenas iniciais ficam em maiusculo


frase = input('Frase: ')
tam = len(frase)
saida = frase[::-1]
print('\nFrase invertida:')
print(saida)


# fatia a mensagem em outros ellementos
