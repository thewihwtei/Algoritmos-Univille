alunos = {}

q = int(input("Digite a quantidade de alunos: "))

for i in range(q):
    nome = input("Digite o nome do aluno: ")

    n1 = float(input("Digite a nota N1: "))
    n2 = float(input("Digite a nota N2: "))
    n3 = float(input("Digite a nota N3: "))
    n4 = float(input("Digite a nota N4: "))

    alunos[nome] = [n1,n2,n3,n4]

for nome, notas in alunos.items():
    menor = min(notas)
    
    notas.remove(menor)

    media = sum(notas) / 3

    if media >= 6.0:
        print(f"{nome}: Aprovado - Média: {media:.2f}")
    else:
        print(f"{nome}: Reprovado - Média: {media:.2f}")