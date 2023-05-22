

m = [0,15,30,5,12], # percurso 1
[15,0,10,17,28], # percurso 2
[30,10,0,3,11], # percurso 3
[5,17,3,0,80], # percurso 4
[12,28,11,80,0] # percurso 5

# Definição da ordem da matriz
n =  5

# Leitura do percurso e soma das distâncias
soma = 0
print('\nDigite as cidades do percurso a percorrer (ou 0 para sair)')
orig = int(input("digite a origem do seu percurso (de 1 a a 5)"))
while True:
    dest = int(input("digite os destinos que pretendo percorrer (de 1 a 5 )"))
    if dest == 0:
        break
    soma += m[orig-1][dest-1]
    orig = dest

# Exibição do resultado
print(f'\nDistancia percorrida: {soma} km')