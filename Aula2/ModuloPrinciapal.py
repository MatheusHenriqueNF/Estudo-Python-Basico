from Aula2.IdentificacaoDeFuncoes import *
minhaLista=[]

print("Preenchendo")
preencherInventario(minhaLista)

print("Exibindo")
exibirInventario(minhaLista)

print("Pesquisando")
localizarPorNome(minhaLista)

print("Alterando")
depreciarPorNome(minhaLista, 20)
print("Excluindo")
print(excluirPorSerial(minhaLista))
exibirInventario(minhaLista)

print("Resumindo")
resumirValores(minhaLista)
