qh = float(input("Qual seu salário por hora? "))
ht = float(input("Quantas horas você trabalha? "))

salarioB = qh * ht
ir = salarioB*0.11
inss = salarioB*0.08
sindicato = salarioB*0.05
vt = ir+inss+sindicato
salarioL = salarioB-vt

print(ir, inss, sindicato)
print(salarioL)