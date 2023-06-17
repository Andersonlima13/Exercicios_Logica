"""crie um programa que abrevie o nome do usuario ex : anderson s. lima"""

nome = input('Nome:\n').upper()
sobrenome = input('sobreNome:\n').upper()

parte = sobrenome.split()
n = len(parte)
saida = parte[-1][0]
print(saida)




