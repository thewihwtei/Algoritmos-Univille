n = int(input("Digite um número: "))

print("Tabuada do ",n)
for i in range(1, 11, +1):
    mult = n*i
    print(n," x ", i," = ", mult)