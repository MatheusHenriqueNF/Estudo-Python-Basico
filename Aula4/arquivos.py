import json

dic = {
    "CHAVES":["CHAVES DO 8", "14/04/2017", "RECEP_01"],
    "QUICO":["QUICO FLORES", "24/04/2017", "RAIOX_01"],
    "FLORINDA":["FLORINDA", "18/04/2017", "RECEP_03"],
}
with open("bd1.json", "w") as file:
    json.dump(dic,file)

# with open('bd.json', 'r') as arquivo:
#
    # dic = json.load(arquivo)
    # for chave, dados in dic.items():
    #     print(chave, " " + str(dados))