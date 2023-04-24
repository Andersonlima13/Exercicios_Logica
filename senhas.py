SenhaCorreta = "abcd"
Erros = 0
while True:
    NovaSenha = input("digite uma senha")
    if NovaSenha != SenhaCorreta:
        Erros = Erros +1
        if Erros == 3:
            print("numero maximo de erros atingidos")
            break
    elif NovaSenha == SenhaCorreta:
        print(f"SenhaCorreta é a senha correta")