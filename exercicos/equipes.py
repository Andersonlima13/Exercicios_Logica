'O programa deve ler duas equipes e declara o vencedor , que deve ser aquele com 2 pontos a mais que a outra equipe'
'o mesmo ja  atigindo 25 pontos'



flag = 25
print("digite a quantia de pontos")
   
A = 0
B = 0

while True:
    Equipe = input("qua equipe recebe os pontos ?") 
    if Equipe == "A":
       pontos = int(input(": ")) 
       A = A + pontos
       print(f' A equie {Equipe} tem {pontos} pontos')
       if A == 25 and B + 2 <= A:
        print("a equipe A venceu")
        break
    elif Equipe == "B":
        pontos = int(input(": "))
        B = B + pontos
        print(f' A equie {Equipe} tem {pontos} pontos')
        if B == 25 and A + 2 <= B:
            print("equipe b ganhou")
            break
    
