'''Informe o código e a quantidade dos itens.
Para encerrar, digite o código "X"

Código: H
Quantidade: 3

Código: B
Quantidade: 2

Código: X

Total a pagar: R$ 29.00
'''


flag = 'X'
total_geral = 0
print(f'Informe o código e a quantidade dos itens.\nPara encerrar, digite o código "{flag}"')
while True:
    cod = input('\nCódigo: ').upper()
    if cod == flag:
        break
    quant = int(input('Quantidade: '))
    if cod == 'H':
        preco = 5.00
    elif cod == 'C':
        preco = 6.00
    elif cod == 'B':
        preco = 7.00
    else:
        preco = 4.00
    total_item = preco * quant
    total_geral = total_geral + total_item
print(f'\nTotal a pagar: R$ {total_geral:.2f}')