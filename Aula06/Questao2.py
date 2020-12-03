"""Faça o código que tenha a função que recebe três parâmetros: inicio,
fim e passo e faz a contagens Seu programa realiza três contagens
através da função criada:
a. De 1 até 10, de 1 em 1
b. De 10 até 0, de 2 em 2
c. Um contagem personalizada"""


def contador(inicio, fim, passo=1):
    if passo >= 1:
        print(inicio)
        for i in range(inicio, fim):
            inicio = inicio + passo
            print(inicio)
            if (inicio <= fim):
                break
    else:
        print(inicio)
        for i in range(fim, inicio):
            inicio = inicio + passo
            print(inicio)
            if inicio > 0:
                break
                


contador(1,10) # De 1 até 10, de 1 em 1
contador(10, 1, -2) # De 10 até 0, de 2 em 2
contador(1, 100, 10) # 
