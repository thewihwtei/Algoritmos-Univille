colonia_a = 4
colonia_b = 10
dias = 0

while colonia_a < colonia_b:
    colonia_a = colonia_a * 1.03
    colonia_b = colonia_b * 1.015 
    dias += 1

print("Quantidade de dias:", dias)