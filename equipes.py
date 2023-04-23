flag = 25


while True:
	Equipe = input("digite qual equipe recebe os pontos")
	if Equipe == "A":
         pontos = int(input("digite a quantidade de pontos"))
        if pontos == flag:
		print("equipe a venceu")
	elif Equipe == "B":
		equipeB = pontos
		if pontos == flag:
			print("equipe b venceu")