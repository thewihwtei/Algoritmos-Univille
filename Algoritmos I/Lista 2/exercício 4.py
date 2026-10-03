sal = float(input("Digite o valor do salário: "))

if sal >= 1500:
    per = 5
elif sal >= 700:
    per = 10
elif sal > 280:
    per = 15
else:
    per = 20
    
aumento = sal*per/100
print("Salário antes do reajuste: ",sal)
print("Aumento: 5%")
print("Valor do aumento: ",sal*0.05)
sal = sal+(sal*0.05)
print("Novo salário: ",sal)