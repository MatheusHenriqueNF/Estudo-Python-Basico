

def cadastrar():
    resposta = "sim"
    boletim = []

    while resposta == "sim":

        notas = []

        nome_aluno = input("Digite o nome do aluno: ")
        quantidade_nota = int(input("Digite a quantidade de notas do aluno: "))

        media = 0;

        for i in range (quantidade_nota):
            nota_aluno = float(input(f"Digite o nota {i + 1} do aluno: "))
            notas.append(nota_aluno)
            media += nota_aluno

        media = media / quantidade_nota

        boletim.append([nome_aluno, notas, media])

        resposta = input("Deseja inserir um novo aluno?").lower()

    return boletim

def boletim(boletim_aluno):

    for alunos in boletim_aluno:

        nome, notas, media = alunos

        print(f"\nNome: {nome}")
        print(f"Notas: {notas}")

        if media <= 5.9:
            print(f"A média foi {media:.2f}. REPROVADO.")
        elif media >= 6:
            print(f"A média foi {media:.2f}. APROVADO.")

def buscar(boletim_aluno):

    busca = input("Digite o nome do aluno: ")
    encontrado = False

    for aluno in boletim_aluno:
        nome, notas, media = aluno

        if busca == nome:
            print(f"\nNome: {nome}")
            print(f"Notas: {notas}")

            if media <= 5.9:
                print(f"A média foi {media:.2f}. REPROVADO.")
            else:
                print(f"A média foi {media:.2f}. APROVADO.")

            encontrado = True
            break

    if not encontrado:
        print("Aluno não encontrado.")

    print("\n\nPrograma finalizado!")


if __name__ == "__main__":
    boletim_aluno = cadastrar()
    boletim(boletim_aluno)
    buscar(boletim_aluno)