resposta = "SIM"  # Inicializa a variável

while resposta.upper() == "SIM":  # Enquanto a resposta for "SIM" (ignorando maiúsculas/minúsculas)
    print("Executando o loop...")

    resposta = input("Deseja continuar? (SIM/NAO): ").strip()  # Pergunta novamente e remove espaços extras

print("Loop encerrado.")  # Quando o usuário digitar algo diferente de "SIM", o loop para
