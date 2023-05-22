'''Uma certa empresa pretende verificar se os seus empregados estarão
qualificados ou não para aposentadoria em 2022.
Para estar em condições, um dos seguintes requisitos deve ser satisfeito:
• Ter no mínimo 65 anos de idade; ou
• Ter trabalhado no mínimo 30 anos; ou
• Ter no mínimo 60 anos e ter trabalhado no mínimo 25 anos.
Com base nas informações acima, faça um programa para:
• Ler o nome do empregado, o ano de nascimento e o ano de seu ingresso
na empresa.
• Calcular e exibir a idade e o tempo de trabalho do empregado (estimado
ao final de 2021)
• Exibir a mensagem “Pode Requerer Aposentadoria” se atender aos
requisitos ou “Não Pode Requerer Aposentadoria” caso contrário.
Ao final de cada execução, o programa deverá perguntar se o usuário deseja
fazer nova verificação. Se sim, o programa deverá repetir tudo novamente,
caso contrário deverá encerrar.'''


flag = "x"
while True:
    Nome = input("digite seu nome")
    dataNascimento = int(input("data de nascimento"))
    Dataingresso = int(input("digite o ano que esntrou na empresa"))
    idade = int(input("digite sua idade "))
    TempoTrabalho = int(input("digite o tempo de trabalho"))
    if idade <= 65:
        print("Idade para se aposentar atingida")
        cont = input("digite x para encerrar")
        if cont == flag:
            break
    elif TempoTrabalho == 30:
        print("Tempo de trabaho atingido para aposentar")
        cont = input("digite x para encerrar")
        if cont == flag:
            break
    elif TempoTrabalho == 25 and idade <= 60:
        print("Tempo de trabaho e idade atingido para aposentar")
        cont = input("digite x para encerrar")
        if cont == flag:
            break
    else:
        print("requisitos ainda não atigindos")
        cont = input("digite x para encerrar")
        if cont == flag:
            break
        



