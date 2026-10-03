nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))

if nota1<0 or nota2<0 or nota1>10 or nota2>10:
    print('as notas devem ser entre 0 e 10')
else:
    media = (nota1 + nota2) /2
    if media >=9 and media <=10:
        conceito = 'A'
    elif media >=7.5 and media <9:
        conceito = 'B'
    elif media >=6 and media <7.5:
        conceito = 'C'
    elif media >=4 and media <6:
        conceito = 'D'
    else:
        conceito = 'E'

if conceito =='A' or conceito =='B' or conceito =='C':
    print("Aprovado")
else:
    print("Reprovado")