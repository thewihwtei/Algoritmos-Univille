alunos = {}

while True:
    matricula = int(input("Digite o número da matrícula (0 para sair): "))

    if matricula == 0:
        break

    nome = input("Digite o Nome: ")
    idade = int(input("Digite a Idade: "))
    curso = input("Digite o Curso: ")

    alunos[matricula] = [nome,idade,curso]

print(alunos)