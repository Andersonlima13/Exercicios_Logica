flag = "x"
ingresso = 0
while True:
    nome = input("digite seu nome:   ")
    if nome == flag:
        break
    sexo = input("digite o sexo:  ")
    if sexo == "M":
        ingresso = ingresso + 50
    elif sexo == "F":
        ingresso =  ingresso + 20
        
    
   
print(ingresso)