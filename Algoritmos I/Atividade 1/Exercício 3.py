distancia = float(input("Digite a distância em Km: "))
velocidade_media = float(input("Digite a velocidade média em km/h: "))

tempo = distancia / velocidade_media
tempo_s = int(tempo * 3600)
segundos = int(tempo_s % 60)
minutos = int(tempo_s / 60)
horas = int(tempo_s / 3600)

print("O tempo estimado é de %05d:%02d:%02d horas" % (horas, minutos, segundos))