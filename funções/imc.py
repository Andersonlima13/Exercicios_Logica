''''progeama que retorna o imc'''
def calc(altura,peso):
    soma = altura * altura
    imc = peso/soma
    return imc

m = calc(1.68,70)
print(m)