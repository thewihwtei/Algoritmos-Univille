idade = int(input("Informe a idade: "))
cont1 = 0
cont2 = 0
cont3 = 0
cont4 = 0

while idade>100:
    if idade>=0 and idade<=25:
        cont1 += 1
    elif idade>25 and idade<=50:
        cont2 += 1
    elif idade>50 and idade<=75:
        cont3 += 1
    elif idade>76 and idade<=100:
        cont2 += 1
    else:
        pass
    idade = int(input("Informe a idade: "))

print("Entre 0 e 25: ",cont1)
print("Entre 26 e 50: ",cont2)
print("Entre 51 e 75: ",cont3)
print("Entre 76 e 100: ",cont4)