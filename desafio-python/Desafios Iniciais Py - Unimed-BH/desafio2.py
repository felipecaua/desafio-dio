valores = input().split() 

participantes = int(valores[0])
cachorros_quente = int(valores[1])

media = float(participantes / cachorros_quente)
print(f"{media:.2f}")
