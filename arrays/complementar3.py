n = 6

vetor = []

for i in range(n):
    num = int(input("digite o valor a ser adcionado no vetor :  "))
    while num in vetor:
        num = int(input("O número já foi digitado. Digite outro número: "))
    vetor = vetor + [num]
    

print(vetor)
