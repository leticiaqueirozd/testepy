# DECISÃO: se acontecer isso faca isso, se nao acontecer nada faca nada
# if, else, elif (else - if)
idade = 18

if (idade) > 18:
    print("é maior de idade")
elif (idade == 18):
    print("tem 18 anos")
else:
    print("é menor de idade")
print("\n")


# REPETICÃO: loop - percorrer dados e exibir na tela
# while, for
x = 10
while x <= 15:
    print(x)
    x += 1

print("\n")

for x in range(15):
    print(x)
print("\n")

# MISCELENEA: parar ou continuar a execucao de um loop
x = 10
while x <= 15:
    print(x)
    x += 2
    if (x > 3):
        break