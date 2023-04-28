'''escreva m programa que leia 3 notas dos alunos e desconsidere a menor , imprimindo o conceito A B C D OU E'''
nota1 = int(input("digite a primeira nota"))
nota2 = int(input("digite a segunda nota"))
nota3 = int(input("digite a terceira nota"))

menor = nota1
if menor > nota2:
    nota2 = menor
if menor > nota3:
    nota3 = menor

soma = nota1+nota2+nota3 - menor
media = soma/2

if media <= 100 and media <= 90:
    media = "conceitoA"
elif media <= 89 and media <= 80:
    media = "conceitoB"
elif media <= 79 and media <= 60:
    media = "conceitoC"
elif media <= 59 and media <= 40:
    media = "conceitoD"
elif media <= 39 and media <= 0:
    media = "conceitoE"

if media == "conceitoA" or "conceitoB" or "conceitoC":
    print("aprovdo")
else:
    print("reprovado")
    