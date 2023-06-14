''''progeama que retorna o imc'''
def calc(altura,peso):
    soma = altura * altura
    imc = peso/soma
    if imc < 18.5:
        return "abaixo do peso"
    elif imc < 24.9 and imc >= 18.5:
        return "peso ideal"
    elif imc < 29.9 and imc >= 25:
        return "sobrepeso"
    elif imc >= 30:
        return "obesidade"
    print(imc)
    

m = calc(1.68,70)
print(m)
