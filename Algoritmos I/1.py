estoque = {}

while True:
    codigo = int(input("Digite o código da peça (0 para sair): "))

    if codigo == 0:
        break

    quantidade = int(input("Digite a quantidade disponível: "))

    if codigo in estoque:
        print("Código já cadastrado!")
    else:
        estoque[codigo] = quantidade

for codigo, quantidade in estoque.items():
    print(codigo, ": ", quantidade)