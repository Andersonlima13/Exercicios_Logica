email = input('E-mail: ')

ind = email.find('@')
login = email[:ind]
dominio = email[ind+1:]

print('Login:',login)
print('Domínio:',dominio)