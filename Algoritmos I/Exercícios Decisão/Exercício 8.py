nome = input("Digite o nome do candidato: ")

n1 = float(input("Digite a nota de Matemática: "))
n2 = float(input("Digite a nota de Português: "))
n3 = float(input("Digite a nota de Conhecimentos Gerais: "))

media = (n1 + n2 + n3)/3

print("Nome do candidato:",nome)
print("Matemática:",n1)
print("Português:",n2)
print("Conhecimentos Gerais:",n3)
print("Média Final:",media)

if media >= 7 and n1>5 and n2>5 and n3>5:
    print("Aprovado!")
else:
    print("Reprovado!")