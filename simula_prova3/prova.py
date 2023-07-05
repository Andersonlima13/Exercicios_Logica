#Função primo
def primo(n):
    cont = 0
    for i in range(1,n+1):
        if n % i == 0:
            cont = cont+1
    if cont > 2:
        return n

#Programa principal

for i in range(1,101):
    numeros = primo(i)
    print(numeros)
