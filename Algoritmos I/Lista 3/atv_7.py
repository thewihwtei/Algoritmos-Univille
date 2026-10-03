gabarito = ['D','A','C','B','A','D','C','C','A','B']
respostas = []
ponto = 0

for i in range(10):
    res = input('Resposta: ')
    respostas.append(res)

for i in range(10):
    if respostas[i] == gabarito[i]:
        ponto += 1

print('Nota: ', ponto)