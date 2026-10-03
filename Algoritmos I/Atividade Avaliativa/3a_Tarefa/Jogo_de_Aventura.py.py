print("MISSÃO ESPACIAL\n")

nome = input("Digite o nome do comandante: ")

print(f"\nComandante {nome}, sua nave esta sem combustivel suficiente!")
print("Você precisa tomar decisões rápidas para sobreviver.\n")

print("Você pode:")
print("1 - Tentar pousar em um planeta desconhecido")
print("2 - Continuar viajando no espaço")

escolha1 = input("\nEscolha (1 ou 2): ")

if escolha1 == "1":
    print("\nVocê pousou em um planeta estranho.")
    print("Ao sair da nave, encontra duas opções:")
    print("1 - Explorar uma floresta alienígena")
    print("2 - Entrar em uma base abandonada")

    escolha2 = input("\nEscolha (1 ou 2): ")

    if escolha2 == "1":
        print("\nCriaturas alienígenas aparecem!")
        print("Você corre de volta para a nave.")
        print("MISSÃO FRACASSADA.")
    
    elif escolha2 == "2":
        print("\nNa base abandonada você encontra combustível.")
        print("Sua nave foi abastecida!")
        print("VOCÊ SOBREVIVEU E VENCEU!")
    
    else:
        print("\nEscolha inválida.")
        print("FIM DE JOGO.")

elif escolha1 == "2":
    print("\nVocê continua viajando pelo espaço.")
    print("Um sinal misterioso aparece no radar.")
    print("1 - Seguir o sinal")
    print("2 - Ignorar o sinal")

    escolha2 = input("\nEscolha (1 ou 2): ")

    if escolha2 == "1":
        print("\nVocê encontra uma estação espacial cheia de tesouros.")
        print("VOCÊ VENCEU!")
    
    elif escolha2 == "2":
        print("\nSua nave fica sem combustível.")
        print("Você ficou perdido no espaço.")
        print("FIM DE JOGO.")
    
    else:
        print("\nEscolha inválida.")
        print("FIM DE JOGO.")

else:
    print("\nEscolha inválida.")
    print("FIM DE JOGO.")