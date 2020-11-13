# Calcular uma prestação de atraso, utilizando a fórmula: PRESTAÇÃO = VALOR + (VALOR * (TAXA/100) * TEMPO) 

valor = float(input('Informe o valor: '))
taxa = float(input('Informe a taxa (%): '))
tempo = int(input('Informe o tempo (dias): '))

prestacao = valor + (valor * (taxa/100) * tempo)

print(f'A sua prestação ficou de {prestacao}.')