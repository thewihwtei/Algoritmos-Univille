import random

numero = random.randint(1, 10)

jogador1 = int(input("Jogador 1, digite um número de 1 a 10: "))
jogador2 = int(input("Jogador 2, digite um número de 1 a 10: "))
jogador3 = int(input("Jogador 3, digite um número de 1 a 10: "))

print("Número sorteado:", numero)

if jogador1 == numero:
    print("Jogador 1 ganhou!")

if jogador2 == numero:
    print("Jogador 2 ganhou!")

if jogador3 == numero:
    print("Jogador 3 ganhou!")

if jogador1 != numero:
    if jogador2 != numero:
        if jogador3 != numero:
            print("Ninguém ganhou!")