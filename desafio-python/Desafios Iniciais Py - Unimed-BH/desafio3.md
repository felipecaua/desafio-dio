valores = input().split()

tempo = int(valores[0])
km_por_hora = int(valores[1])

quantidade_de_litros = float((tempo * km_por_hora) / 12)
print(f"{quantidade_de_litros:.3f}")
