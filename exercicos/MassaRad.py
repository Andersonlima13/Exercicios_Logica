Tempo = 0
Massa = int(input("digite a quantidade de massa"))

while True:
    Massa = Massa/ 2
    if Massa > 0.5:
        Tempo = Tempo + 50
        print(Tempo)
    if Massa < 0.5:
        print(Tempo)