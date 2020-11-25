import random as rd

numeros_sorteados = []
num = int(input('Quantos jogos você quer sortear? '))
for y in range(1, num + 1):
    while True:
        numero = rd.randint(1, 60)
        if numero not in numeros_sorteados:
            numeros_sorteados.append(numero)

        if len(numeros_sorteados) == 6:
            break
    
    print(f'Jogo {y}: {numeros_sorteados}')
    del(numeros_sorteados[0:6])

