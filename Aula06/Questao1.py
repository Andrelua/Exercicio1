import random as rd


def pedra(i):
    if i == 1:
        print('Empate') 
    elif i == 2:
        print('Derrota')
    elif i == 3:
        print('Vitória')

def papel(i):
    if i == 1:
        print('Vitória') 
    elif i == 2:
        print('Empate')
    elif i == 3:
        print('Derrota')

def tesoura(i):
    if i == 1:
        print('Vitória')
    elif i == 2:
        print('Vitória') 
    elif i == 3:
        print('Empate')

def jokenpo():
    while True:
        num = rd.randint(1,3)

        print('Qual você escolhe? ')
        escolha = int(
            input("1 - Pedra \n"
            "2 - Papel \n"
            "3 - Tesoura \n"
            "0 - sair \n")
            )
        if escolha == 1:
            pedra(num)
        elif escolha == 2:
            papel(num)
        elif escolha == 3:
            tesoura(num)

        if escolha == 0:
            print("Você saiu do jogo, até a próxima!!") 
            break

jokenpo()