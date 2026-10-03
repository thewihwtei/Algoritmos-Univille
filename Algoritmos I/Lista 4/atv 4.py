temp = float(input("Digite a temperatura: "))
soma = 0
cont = 0

while temp != 273:
    soma += temp
    cont += 1
    temp = float(input("Digite a temperatura: "))

media = soma/cont
print(round(media, 2))