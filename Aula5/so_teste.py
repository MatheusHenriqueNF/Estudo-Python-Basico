# import platform
# import datetime
import getpass

# print("Distribuição do Sistema Operacional.: ", platform.platform())
# print("Nome do Sistema Operacional.........: ", platform.system())
# print("Versão do Sistema Operacional.......: ", platform.release())
# print("Arquitetura.........................: ", platform.architecture())
# print("Nome do Computador..................: ", platform.node())
# print("Tipo de Máquina.....................: ", platform.machine())
# print("Processador.........................: ", platform.processor())
# print("Versão do Python....................: ", platform.python_version())
#
# print(datetime.date.today())

print(getpass.getuser())
print(getpass.getpass("Digite sua senha"))


if usuario == 'usertricaster' and senha == 'HELLO':
    print("Bem-vindo")
else:
    print("Você não acesso")