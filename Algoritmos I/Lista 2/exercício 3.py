print("Qual turno você estuda? ")
print("M - Matutino")
print("V - Vespertino")
print("N - Noturno")
t = input().upper()

if t=="M":
    print("Bom dia!")
elif t=="V":
    print("Boa tarde!")
elif t=="N":
    print("Boa noite!")
else:
    print("Valor inválido")