

resposta = "sim"

while resposta == "sim":
    nome = input("Digite o nome do aluno: ")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    nota4 = float(input("Digite a quarta nota: "))
    media = (nota1 + nota2 + nota3 + nota4) / 4
    if media <= 5.9:
        print(f"A média foi {media}. REPROVADO.")
    elif media >= 6:
        print(f"A média foi {media}. APROVADO.")

    resposta = input("Deseja inserir um novo aluno?").lower()

