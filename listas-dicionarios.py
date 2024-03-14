#LISTAS 
listaDeFrutas = ["banana", "uva", "goiaba"]
# print(listaDeFrutas [0])

listaDeFrutas.append("pera")
listaDeFrutas.insert(2, "mamao")
listaDeFrutas.remove("goiaba")

for fruta in listaDeFrutas:
    print(fruta)

#DICIONARIO - achar valor
diciPessoas = {
    "nome": "Leticia",
    "idade": 22,
    "cidade": "Recife"
}

print(diciPessoas["idade"])