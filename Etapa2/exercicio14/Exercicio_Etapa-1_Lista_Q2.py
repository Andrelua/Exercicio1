'''Todo mês Mateus economiza um certo valor indefinido do seu 
salario, ele deseja saber qual mês do ano ele econimizou
o maior e o menor valor e quanto foi. Então faça um programa
 utilizando lista para resolver esse problema.'''
salario = 1220
economia = []
for i in range(0, 12):
    eco = int(input(f"Quantos porcentos ele economizou no {i+1}º mês ? "))
    valoreco = salario * (eco / 100)
    economia.append(valoreco)

print(f"A maior economia foi de {max(economia)} e foi no {economia.index(max(economia))+1}º mês.")
print(f"A menor economia foi de {min(economia)} e foi no {economia.index(min(economia))+1}º mês.")
