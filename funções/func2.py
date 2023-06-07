def notas(a,b,c):
    somador = a + b + c
    media = somador/3
    return media

s = notas(10,8,4)

def conceito(media):
    if 8 <= media:
        return "A"
    if 5 <= media and media < 8:
        return "B"
    if 5 < media:
        return "C"
conc = conceito(s)

print(s)
print(conc)