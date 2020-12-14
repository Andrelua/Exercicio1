"""
Faça um programa que ajude um jogador da Mega Sena a criar palpites. O
programa vai perguntar quantos jogos serão gerados e vai sortear 6 números
entre 1-60 para cada jogo, cadastrando tudo em uma lista composta.
Exemplo:
Quantos jogos você quer sortear? 2
Jogo 1: [4,8,10,20,26,38]
Jogo 2: [14, 20, 43, 35, 38,47]

Obs: o número não pode se repetir no mesmo jogo. Mas, não tem problema se
repetir em outro jogo.
Além de exibir na tela o resultado do palpite.
Você criar um arquivo com os mesmos resultados.
"""
from os import close
import random as rd

with open('Palpite.txt', 'w') as arquivo:
    numeros_sorteados = []
    num = int(input('Quantos jogos você quer sortear? '))
    for y in range(1, num + 1):
        while True:
            numero = rd.randint(1, 60)
            if numero not in numeros_sorteados:
                numeros_sorteados.append(numero)

            if len(numeros_sorteados) == 6:
                break
        print(f"Jogo {y}: {str(numeros_sorteados)}\n")
        arquivo.write(f"Jogo {y}: {str(numeros_sorteados)}\n")
        del(numeros_sorteados[0:6])
    
    arquivo.close()
