par = 0
impar = 0
produtos = []

for i in range(5):
    id = int(input('Insira o ID: '))
    produtos.append(id)

for i in produtos:
    if i % 2 == 0:
        par += 1
    else:
        impar += 1

print(produtos)
print('Doces: ',par)
print('Amargos: ', impar)