val_hora = float(input("Digite o valor da hora trabalhada: "))
qtdd_hora = int(input("Digite a quantidade de horas trabalhadas: "))
inss_porc = int(input("Digite a porcentagem de desconto de INSS: "))

inss = inss_porc/100

sal_bruto = qtdd_hora*val_hora
sal_liq = sal_bruto-(sal_bruto*inss)

print("Salário líquido: R$ ",sal_liq)