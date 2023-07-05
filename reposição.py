empate = 0
vitoria_mandante = 0
vitoria_visitante = 0
total_gols = 0

for i in range(3):
    time_visitante = input("digite o nome do visitiante: ")
    time_mandante = input("digite o nome do mandante: ")
    gols_visitante = int(input("digite a quantidade de gols do visitante: "))
    gols_mandante = int(input("digite a quantidade de gols do mandante : "))
    total_gols = gols_mandante + gols_visitante
    if gols_mandante > gols_visitante:
        vitoria_mandante = vitoria_mandante + 1
    elif gols_visitante > gols_mandante:    
        vitoria_visitante = vitoria_visitante + 1
    else:
        empate = empate + 1
    
    
print(vitoria_visitante)
print(vitoria_mandante)
print(total_gols)
print(empate)        