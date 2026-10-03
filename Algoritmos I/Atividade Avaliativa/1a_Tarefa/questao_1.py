# Entrada de dados
nome = input("Digite o nome do cliente: ")
diarias = int(input("Digite o número de diárias: "))

if diarias < 0:
    print("Número Inválido!")
else:
    valor_diaria = 60

    if diarias > 15:
        taxa = 5.50
    elif diarias == 15:
        taxa = 6.00
    else:
        taxa = 8.00

    total = diarias * (valor_diaria + taxa)

    print("Nome do cliente:", nome)
    print("Total da conta: R$", total)