contatos = {}

while True:
    nome = input("Digite o nome do contato: ")

    if nome == "":
        break

    idade = int(input("Digite a idade: "))
    telefone = input("Digite o telefone: ")

    contatos[nome] = {
        "idade": idade,
        "telefone": telefone
    }

for nome in sorted(contatos):
    print(nome, contatos[nome])

menores = {}
maiores = {}

for nome, dados in contatos.items():
    if dados["idade"] < 18:
        menores[nome] = dados
    else:
        maiores[nome] = dados

del contatos

print("\nCONTATOS MENORES DE 18 ANOS:")
print(menores)

print("\nCONTATOS COM 18 ANOS OU MAIS:")
print(maiores)