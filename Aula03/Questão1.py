lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3,-52]
maior = 0
for i in lista:
    if i > maior:
        maior = i

menor = 99999999999
for i in lista:
    if i < menor:
        menor = i

pares = []
for i in range(0, 15):
    if (i % 2 == 0):
        pares = i       

ocorrencia = 0
for i in range(0, 15):
    if (lista[0] == lista[i]):
        ocorrencia += 1

soma = 0
for i in range(0, 15):
    soma = soma + lista[i]

media = soma/15

soma_negativos = 0
i = 0
for i in range(0, 15):
    if lista[i] < 0:
        soma_negativos = soma_negativos + lista[i]
    i += 1

print(f"Maior elemento: {maior}")
print(f"Menor elemento: {menor}")
print(f"Números pares: {pares}")
print(f"Ocorrência do primeiro elemento na lista: {ocorrencia}")
print(f"Média dos elementos: {media:.2f}")
print(f"Soma dos negativos: {soma_negativos}")
