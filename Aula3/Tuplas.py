usuario = {}
emails = ["xpto@xyz.com", "xkcd@phd.com"]

tupla = list(enumerate(emails))

for chave in range(0, len(tupla)):
    print("Email: ",tupla[chave][1])
    usuario[tupla[chave]] = [input("Digite o nome: "), input("Digite o nivel: "),]

for chave, dado in usuario.items():
    print("Usuario: ",dado[0])
    print("Email: ",dado[1])
    print("Nome: ",dado[0])
    print("Nivel: ",dado[1])