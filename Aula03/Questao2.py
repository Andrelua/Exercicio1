"""Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um
par de dados, obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11,
você um "natural" e ganhou. Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de
"craps" e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu
"Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número novamente.
Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente."""

import random as rd
import time

print('+='*15)
print('Bem-vindo(a) ao jogo de Craps.')
print('+='*15)
print('\n')
print('+='*20)
print('Peço que se identifique pelo seu nome.')
print('+='*20)
nome_jgr = input('Nome: ')

pontos = 0
rodada = 1

while True:

    print('+='*15)
    print('Aguarde, jogando os dados...')
    print('+='*15)
    print('\n')

    time.sleep(2)
    dado1 = rd.randint(1,6)
    dado2 = rd.randint(1,6)
    soma_dados = dado1 + dado2

    if ((soma_dados == 7) or (soma_dados == 11)) and (rodada == 1):
        print(f'Você tirou {soma_dados} na primeira rodada.')
        print('Você é um "natural" e ganhou!!!')
        print(f'Parabéns {nome_jgr}!!!!')
        break
    elif soma_dados in [2, 3, 12] and (rodada == 1):
        print(f'Você tirou {soma_dados} na primeira rodada.')
        print('EEEEE deu "craps" e você perdeu!!!')
        print(f'Na próxima quem sabe, {nome_jgr}!!')
        break
    elif soma_dados in [4, 5, 6, 8, 9, 10, 2, 3, 12]:
        print(f'Você tirou {soma_dados}.')
        print(f'{nome_jgr}, você recebeu um ponto!!')
        pontos += 1 
        rodada += 1
        print(f"Você juntou {pontos} pontos.")
    elif (soma_dados == 7) and (rodada != 1):
        print('Que pena, você tirou um 7.')
        print('O jogo acabou !!')
        break
    
