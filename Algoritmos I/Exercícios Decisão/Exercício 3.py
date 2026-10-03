valor_emp = float(input("Digite o valor do empréstimo: "))
n_parc = int(input("Digite o número de parcelas: "))
sal = float(input("Digite o seu salário:"))

valor_parc = valor_emp/n_parc
cond = sal*0.3

if valor_parc <= cond:
    print("Empréstimo aprovado!")
else:
    print("Empréstimo recusado!")