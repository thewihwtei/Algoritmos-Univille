saldo = float(input("Digite o saldo médio do cliente: "))

if saldo < 0:
    print("Saldo inválido!")
else:
    if saldo <= 200:
        percentual = 0
        credito = 0
    elif saldo <= 400:
        percentual = 20
        credito = saldo * 0.20
    elif saldo <= 600:
        percentual = 30
        credito = saldo * 0.30
    else:
        percentual = 40
        credito = saldo * 0.40

    print("=========Resultado=========")
    print("Saldo médio: R$", saldo)
    print("Percentual aplicado:", percentual, "%")
    print("Valor do crédito: R$", credito)
    print("===========================")