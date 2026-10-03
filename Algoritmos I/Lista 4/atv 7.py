numero = int(input("Digite um número inteiro: "))

if numero < 2:
    print(f"{numero} não é um número primo.")
else:
    primo = True

    for i in range(2, numero):
        if numero % i == 0:
            primo = False
            break

    if primo:
        print(f"{numero} é um número primo.")
    else:
        print(f"{numero} não é um número primo.")