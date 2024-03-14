diciPessoas = {
    "nome": "Leticia"
}
try:
    print(diciPessoas["idade"])
except KeyError as e:
    print("Ocorreu um erro")
except Exception as e:
    print("erro")
finally:
    print("FIM")