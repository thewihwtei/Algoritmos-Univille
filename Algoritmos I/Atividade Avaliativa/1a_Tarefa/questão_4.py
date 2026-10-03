valor_compra = float(input("Digite o valor da compra: R$ "))
valor_pago = float(input("Digite o valor pago: R$ "))


troco = int(valor_pago - valor_compra)


notas_100 = troco // 100
resto = troco % 100

notas_10 = resto // 10
resto = resto % 10

notas_1 = resto


print("\n===== TROCO =====")
print(f"Valor da compra: R$ {valor_compra:.2f}")
print(f"Valor pago: R$ {valor_pago:.2f}")
print(f"Valor do troco: R$ {troco:.2f}")

print("\nNotas do troco:")
print(f"Notas de R$100: {notas_100}")
print(f"Notas de R$10 : {notas_10}")
print(f"Notas de R$1  : {notas_1}")