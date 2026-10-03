# Leitura do gabarito
with open("gabarito.txt", "r", encoding="utf-8") as arquivo:
    gabarito = arquivo.readline().strip().split(",")

# Lista para armazenar resultados
classificacao = []

# Leitura dos candidatos
with open("candidatos.txt", "r", encoding="utf-8") as arquivo:
    
    for linha in arquivo:
        
        dados = linha.strip().split(",")

        id_candidato = dados[0]
        nome = dados[1]

        respostas = dados[2:]

        nota = 0

        # Comparação das respostas com o gabarito
        for i in range(len(gabarito)):
            if respostas[i] == gabarito[i]:
                nota += 1

        classificacao.append([id_candidato, nome, nota])

# Geração do arquivo de classificação
with open("classificacao.txt", "w", encoding="utf-8") as arquivo:

    for candidato in classificacao:
        linha = f"{candidato[0]},{candidato[1]},{candidato[2]}\n"
        arquivo.write(linha)

print("Classificação gerada com sucesso!")