nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

if nota1 < 0 or nota2 < 0 or nota3 < 0 or nota1 > 10 or nota2 > 10 or nota3 > 10:
    print("Erro: notas não podem ser negativas!")
else:
    print("Escolha o tipo de média:")
    print("1 - Média Aritmética")
    print("2 - Média Ponderada")

    opcao = int(input("> "))

    if opcao == 1:
        media = (nota1 + nota2 + nota3) / 3
        print("Média Aritmética:", media)

    elif opcao == 2:
        media = (nota1 * 3 + nota2 * 3 + nota3 * 4) / 10
        print("Média Ponderada:", media)

    else:
        print("Opção inválida!")