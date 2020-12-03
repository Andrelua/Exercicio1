

def maior_menor(*argumentos):
    maior = 0
    for i in range(0, len(argumentos)):
        if argumentos[i] > maior:
            maior = argumentos[i]
            

    menor = 9999
    for i in range(0, len(argumentos)):
        if argumentos[i] < menor:
            menor = argumentos[i]
            

    print(f"O MAIOR NÚMERO É {maior} E O MENOR NÚMERO É {menor}.")



maior_menor(1, 3, 5, 6)