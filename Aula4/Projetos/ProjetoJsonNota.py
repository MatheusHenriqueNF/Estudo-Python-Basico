import json
import sys


def salvar_dados(dicionario):
    with open("sistema_alunos.json", "w", encoding="utf-8") as arquivo:
        json.dump(dicionario, arquivo, ensure_ascii=False, indent=4)


def cadastrar(boletim):
    resposta = "sim"

    while resposta == "sim":
        nome = input("Digite o nome do aluno: ")
        if nome in boletim:
            print("Aluno já cadastrado! Digite outro nome.")
            continue

        quantidade_nota = int(input("Digite a quantidade de notas do aluno: "))
        notas = []
        media = 0

        for i in range(quantidade_nota):
            nota_aluno = float(input(f"Digite a nota {i + 1} do aluno: "))
            notas.append(nota_aluno)
            media += nota_aluno

        media /= quantidade_nota
        boletim[nome] = {"Notas": notas, "Média": media}
        salvar_dados(boletim)

        resposta = input("Deseja inserir um novo aluno? (sim/não) ").strip().lower()


def boletim_alunos(boletim):
    for nome, dados in boletim.items():
        print(f"\nNome: {nome}")
        print(f"Notas: {dados['Notas']}")
        print(f"Média: {dados['Média']:.2f}")
        if dados["Média"] <= 5.9:
            print("REPROVADO.")
        else:
            print("APROVADO.")


def buscar(boletim):
    busca = input("Digite o nome do aluno: ")

    if busca in boletim:
        print(f"\nNome: {busca}")
        print(f"Notas: {boletim[busca]['Notas']}")
        print(f"Média: {boletim[busca]['Média']:.2f}")
    else:
        print("Aluno não encontrado.")


def atualizar(boletim):
    busca = input("Digite o nome do aluno: ")
    if busca in boletim:
        print(f"\nNome: {busca}")
        print(f"Notas: {boletim[busca]['Notas']}")
        print(f"Média: {boletim[busca]['Média']:.2f}")

        escolha = int(input("\nQual dado deseja atualizar? 1-[Notas] 2-[Média]: "))

        if escolha == 1:
            pos = int(input("Digite a posição da nota que deseja atualizar (1, 2, 3...): ")) - 1
            if 0 <= pos < len(boletim[busca]["Notas"]):
                nova_nota = float(input("Digite a nova nota: "))
                boletim[busca]["Notas"][pos] = nova_nota
                boletim[busca]["Média"] = sum(boletim[busca]["Notas"]) / len(boletim[busca]["Notas"])
                print(f"Notas atualizadas: {boletim[busca]['Notas']}")
                print(f"Nova média: {boletim[busca]['Média']:.2f}")
            else:
                print("Posição inválida!")
        elif escolha == 2:
            nova_media = float(input("Digite a nova média: "))
            boletim[busca]["Média"] = nova_media
            print(f"Nova média: {boletim[busca]['Média']:.2f}")

        salvar_dados(boletim)
    else:
        print("Aluno não encontrado.")


def acrescentar_nota(boletim):
    busca = input("Digite o nome do aluno: ")
    if busca in boletim:
        nova_nota = float(input("Digite a nova nota: "))
        boletim[busca]["Notas"].append(nova_nota)
        boletim[busca]["Média"] = sum(boletim[busca]["Notas"]) / len(boletim[busca]["Notas"])
        print(f"Notas atualizadas: {boletim[busca]['Notas']}")
        print(f"Nova média: {boletim[busca]['Média']:.2f}")
        salvar_dados(boletim)
    else:
        print("Aluno não encontrado.")


def remover_nota(boletim):
    busca = input("Digite o nome do aluno: ")
    if busca in boletim:
        print(f"\nNome: {busca}")
        print(f"Notas: {boletim[busca]['Notas']}")
        print(f"Média: {boletim[busca]['Média']:.2f}")
        pos = int(input("Digite a posição da nota a ser removida: ")) - 1
        if 0 <= pos < len(boletim[busca]["Notas"]):
            boletim[busca]["Notas"].pop(pos)
            if boletim[busca]["Notas"]:
                boletim[busca]["Média"] = sum(boletim[busca]["Notas"]) / len(boletim[busca]["Notas"])
            else:
                boletim[busca]["Média"] = 0
            print(f"Notas atualizadas: {boletim[busca]['Notas']}")
            print(f"Nova média: {boletim[busca]['Média']:.2f}")
            salvar_dados(boletim)
        else:
            print("Posição inválida!")
    else:
        print("Aluno não encontrado.")


def menu():
    try:
        with open("sistema_alunos.json", "r", encoding="utf-8") as arquivo:
            boletim = json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        boletim = {}

    while True:
        print("\nSISTEMA DE BOLETIM")
        print("Escolha uma opção:\n")
        print("1 - Cadastrar aluno")
        print("2 - Remover nota do aluno")
        print("3 - Adicionar nota do aluno")
        print("4 - Atualizar nota do aluno")
        print("5 - Mostrar boletim de todos os alunos")
        print("6 - Buscar aluno")
        print("7 - Encerrar")

        escolha = input("\nOpção escolhida: ")

        if escolha == "1":
            cadastrar(boletim)
        elif escolha == "2":
            remover_nota(boletim)
        elif escolha == "3":
            acrescentar_nota(boletim)
        elif escolha == "4":
            atualizar(boletim)
        elif escolha == "5":
            boletim_alunos(boletim)
        elif escolha == "6":
            buscar(boletim)
        elif escolha == "7":
            print("Encerrando o programa...")
            break
        else:
            print("Escolha uma opção válida (1 a 7).")


if __name__ == "__main__":
    menu()
