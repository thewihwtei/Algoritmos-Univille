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
    media = sum(notas) / 4

    print(f"\nAluno: {nome}")
    print(f"Notas: {notas[0]:.1f}, {notas[1]:.1f}, {notas[2]:.1f}, {notas[3]:.1f}")
    print(f"Média: {media:.1f}")

    if media >= 6.0:
        print("Situação: Aprovado")
    else:
        print("Situação: Reprovado")