

def controle():

    mouses = [0]*4
    calculo = []
    
    while True:
        menuEntrada = int(input("Situação do mouse: " +
        "\n1 - Necessidade de esfera \n2 - Necessidade de limpeza \n3 - Necessita troca de cabo ou conector" +
        "\n4 - Quebrado ou inutilizado \n0 - Sair: "))
        
        if menuEntrada == 0:
            break
        elif menuEntrada == 1:
            mouses[0] += 1
        elif menuEntrada == 2:
            mouses[1] += 1
        elif menuEntrada == 3:
            mouses[2] += 1
        elif menuEntrada == 4:
            mouses[3] += 1
        
    for i in range(len(mouses)):
        calculo1 = (mouses[i] * 100) / sum(mouses)
        calculo.append(calculo1)
    
    print(f"Quantidade de mouses {sum(mouses)}.")
    print("SITUAÇÃO                  QUANTIDADE                 PERCENTUAL")
    print(f"1 - Necessidade de esfera -        {mouses[0]}                {calculo[0]:.2f}%\n" + 
    f"2 - Necessidade de limpeza -             {mouses[1]}                {calculo[1]:.2f}%\n" + 
    f"3 - Necessita troca de cabo ou conector - {mouses[2]}               {calculo[2]:.2f}%\n" +
    f"4 - Quebrado ou inutilizado -            {mouses[3]}                {calculo[3]:.2f}%")
    

controle()