dados = 0

while dados<=15:
    nota = int(input("Digite uma nota entre 0 e 5:"))

    while nota<0 or nota>5:
        print("Inválido!")
        nota = int(input("Digite uma nota entre 0 e 5:"))
        
    print("Nota registrada!")
    dados += 1

print("Todas as notas cadastradas!")