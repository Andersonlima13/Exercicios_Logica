NumeroPrimo = int(input("digite um numero"))
Divisores = 0
for i in range(1,NumeroPrimo + 1):
    if NumeroPrimo % i == 0:
        Divisores += 1
        print(i)
if Divisores > 2:
     print(f'os valor {NumeroPrimo} é primo sendo assim contem {Divisores} divisores')
elif Divisores <= 2:
    print(f"o valor {NumeroPrimo} não é primo")
    
       
       