'''Tiago nessa Black Friday resolveu comprar um fone de ouvido e 
esta pesquisando o preço em várias lojas. Faça
um programa usando lista onde Tiago ira digitar o nome da loja e o 
valor do fone de ouvido, no final.
Exiba qual loja tem o menor e o maior preço.'''

listaLojas = []
while True:
    lista02 = []
    for i in range(0, 1):
        lista02.append(input("Informe o nome da loja: "))
        lista02.append(int(input("Informe o valor do fone nessa loja: ")))
    listaLojas.append(lista02)
    exit = input("Deseja encerrar (Y/N): ")
    if exit == "Y":
        break

maior = 0
nomeMaior = 0
for i in range(0, len(listaLojas)):
    if listaLojas[i][1] > maior:
        maior = listaLojas[i][1]
        nomeMaior = listaLojas[i][0]

menor = 99999999999
nomeMenor = 0
for i in range(0, len(listaLojas)):
    if listaLojas[i][1] < menor:
        menor = listaLojas[i][1]
        nomeMenor = listaLojas[i][0]

print(f"O maior preço foi da loja {nomeMaior} e foi de {maior}. ")
print(f"O menor preço foi da loja {nomeMenor} e foi de {menor}. ")
