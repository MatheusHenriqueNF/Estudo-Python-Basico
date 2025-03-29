
resposta = "sim"

while resposta == "sim":

    nome = input("Digite o nome do aluno: ")
    quantidade_nota = int(input("Digite a quantidade de notas do aluno: "))
    media = 0;
    i = 1;
    for i in range (quantidade_nota):
        nota = float(input(f"Digite o nota {i + 1} do aluno: "))
        media += nota

    media = media / quantidade_nota
    print(media)
    resposta = input("Deseja inserir um novo aluno?").lower()

print("Programa finalizado!")