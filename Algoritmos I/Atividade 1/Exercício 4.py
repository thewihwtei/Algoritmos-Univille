salario = float(input("Digite o salário atual: "))
p_aumento = float(input("Digite a porcentagem de aumento: "))

aumento = salario * p_aumento/100
novo_salario = salario + aumento

print("Um aumento de %5.2f%% em um salário de R$ %7.2f"%(p_aumento,salario))
print("é igual a um aumento de R$ %7.2f"% aumento)
print("Resultando um novo salário de R$ %7.2f"% novo_salario)