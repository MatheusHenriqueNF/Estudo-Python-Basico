with open("arquivo.txt", 'r', encoding="utf8") as arquivo:
    for linha in arquivo.readlines():
        print(linha)