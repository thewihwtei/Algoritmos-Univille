n1 = float(input("Digite o valor da nota 1: "))
n2 = float(input("Digite o valor da nota 2: "))
n3 = float(input("Digite o valor da nota 3: "))

if n1<0 or n1>10 or n2<0 or n2>10 or n3<0 or n3>10:
    print("Indorme notas válidas entre 0 e 10.")
else:
    media = (n1+n2+n3)/3
    if media == 10:
        print("Aprovado com distinção")
    elif media >= 7:
        print("Aprovado!")
    else:
        print("Reprovado!")
print("Média: ",media)