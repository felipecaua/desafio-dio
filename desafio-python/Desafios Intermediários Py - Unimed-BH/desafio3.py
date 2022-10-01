salario = int(input())
percentual = 0

if salario >= 0 and salario < 600:
  aumento = (salario * 17) / 100
  novo_salario = salario + aumento
  percentual = 17
  
  pf = f"{novo_salario:.2f}" 
  pf2 = f"{aumento:.2f}"   
  
elif salario >= 600.01 and salario < 900:
  aumento = (salario * 13) / 100
  novo_salario = salario + aumento
  percentual = 13
  
  pf = f"{novo_salario:.2f}" 
  pf2 = f"{aumento:.2f}"   

elif salario >= 900.01 and salario < 1500:
  aumento = (salario * 12) / 100
  novo_salario = salario + aumento
  percentual = 12
  
  pf = f"{novo_salario:.2f}" 
  pf2 = f"{aumento:.2f}"   

  
elif salario >= 1500.01 and salario <= 2000:
  aumento = (salario * 10) / 100
  novo_salario = salario + aumento
  percentual = 10
  
  pf = f"{novo_salario:.2f}" 
  pf2 = f"{aumento:.2f}"   
  
elif salario > 2000:
  aumento = (salario * 5) / 100
  novo_salario = salario + aumento
  percentual = 5
  
  pf = f"{novo_salario:.2f}" 
  pf2 = f"{aumento:.2f}"   

else:
  exit()

print(f"Novo salario: {pf}")
print(f"Reajuste ganho: {pf2}")
print(f"Em percentual: {percentual} %")
  