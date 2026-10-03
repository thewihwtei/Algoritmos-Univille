n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

if n1 < n2:
    for i in range(n1 + 1, n2):
        print(i)
elif n2 < n1:
    for i in range(n2 + 1, n1):
        print(i)
else:
    print("Os números são iguais.")