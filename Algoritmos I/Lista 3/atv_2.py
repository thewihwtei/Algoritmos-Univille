papel = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64,3219.08]
cont = 0
soma = 0

for i in papel:
    if i > 3000:
        cont += 1
        soma += i

print("Compras acima de 3.000: ",cont)
porc = int(soma*100/sum(papel))
print(porc,"%")