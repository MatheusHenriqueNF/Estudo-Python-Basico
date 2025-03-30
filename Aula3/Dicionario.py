usuarios = {}
print(usuarios)

usuarios = {"chaves": ["Chaves do 8", "24/12/2017", "Recep_1"],
            "quico": ["Quico das Flores", "20/12/2017", "Raiox_03"]
            }

print(usuarios)

usuarios["florida"] = ["Dona Florinda", "20/12/2017", "Raiox_1"]
print(usuarios)

print("####----####")
print(usuarios.get("quico"))