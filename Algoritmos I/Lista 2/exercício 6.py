l1 = int(input("Digite o lado 1: "))
l2 = int(input("Digite o lado 2: "))
l3 = int(input("Digite o lado 3: "))

if l1==l2==l3:
    print("Equilátero")
elif (l1==l2) or (l1==l3) or (l2==l3):
    print("Isósceles")
else:
    print("Escaleno")