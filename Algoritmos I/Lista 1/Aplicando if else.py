'''3. Construa um programa que leia 2 números reais informados
pelo usuário. Ao fim, o programa deve calcular e imprimir:
a. a soma dos dois valores
b. o produto entre eles

Para essa atividade apresentei outras opções de operações matemáticas para o usuário escolher, entre adição,
subtração, multiplicação e divisão.
'''
n1 = float(input("Digite um número: "))
n2 = float(input("Digie outro número: "))

print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

operacao = float(input("Digite a operação 1/2/3/4: "))

if operacao == 1:
    conta = n1+n2
    print("O resultado é: ", conta)
else:
    if operacao == 2:
        conta = n1-n2
        print("O resultado é: ", conta)
    else:
        if operacao == 3:
            conta = n1*n2
            print("O resultado é: ", conta)
        else:
            if operacao == 4:
                conta = n1/n2
                print("O resultado é: ", conta)
            else:
                print("Operação Inválida!")

'''4. Implemente um programa que converta o valor de uma velocidade média em km/h para m/s. Para isso, o usuário deve
informar o valor da velocidade média. Sabe-se que o fator utilizado para essa conversão é 3,6.

Nessa atividade dei a opção do usuário escolher qual conversão ele deseja fazer, km para m, ou m para km.
'''

vel = float(input("Digite a velocidade: "))

print("Você gostaria de fazer qual conversão?")
print("1 - Quiômetros para Milhas")
print("2 - Milhas para Quilômetros")
opc = int(input("Digite a opção: "))

if opc == 1:
    conv = vel/1.609
    print(vel," Km/h são ",conv," M/h")
if opc == 2:
    conv = vel*1.609
    print(vel," M/h são ",conv," Km/h")