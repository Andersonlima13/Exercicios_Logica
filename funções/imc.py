''''progeama que retorna o imc'''
def calc(altura,peso):
    soma = altura * altura
    imc = peso/soma
    if imc < 18.5:
        return print(f" seu imc é de {imc}, CONDIÇÃO: abaixo do peso")
    elif imc < 24.9 and imc >= 18.5:
        return print(f" seu imc é de {imc}, CONDIÇÃO: peso IDEAL")
    elif imc < 29.9 and imc >= 25:
        return print(f" seu imc é de {imc}, CONDIÇÃO: sobrepeso")
    elif imc >= 30:
        return print(f" seu imc é de {imc}, CONDIÇÃO: obesidade")
    
    

m = calc(1.68,70)
print(m)
