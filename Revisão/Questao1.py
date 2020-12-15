

def intervalo(i, inicio, fim):
    if inicio <= i <= fim:
        return i


def comissao():
    salario = []
    counters = 5
    while True:
        
        vendaBruta = int(input("Venda bruta do vendedor: "))
        retorno = (200 + (0.09 * vendaBruta))

        salario.append(retorno)
        counters -= 1
        if counters == 0:
            counters = 5
            saida = input("Deseja encerrar (Y/N)? ")
            if saida == 'Y':
                break
    # print(salario) Teste
    contagem(salario)

def contagem(salarios):
    contadorA = 0
    contadorB = 0
    contadorC = 0
    contadorD = 0
    contadorE = 0
    contadorF = 0
    contadorG = 0
    contadorH = 0
    contadorI = 0
    for i in range(len(salarios)):
        if salarios[i] == intervalo(salarios[i], 200, 299):
            contadorA += 1
        if salarios[i] == intervalo(salarios[i], 300, 399):
            contadorB += 1
        if salarios[i] == intervalo(salarios[i], 400, 499):
            contadorC += 1
        if salarios[i] == intervalo(salarios[i], 500, 599):
            contadorD += 1
        if salarios[i] == intervalo(salarios[i], 600, 699):
            contadorE += 1
        if salarios[i] == intervalo(salarios[i], 700, 799):
            contadorF += 1
        if salarios[i] == intervalo(salarios[i], 800, 899):
            contadorG += 1
        if salarios[i] == intervalo(salarios[i], 900, 999):
            contadorH += 1
        if salarios[i] == intervalo(salarios[i], 1000, 9999):
            contadorI += 1

    print(f"\nIntervalo A (200, 299): {contadorA} \n" + 
        f"Intervalo B (300, 399): {contadorB} \n" +
        f"Intervalo C (400, 499): {contadorC} \n" +
        f"Intervalo D (500, 599): {contadorD} \n" +
        f"Intervalo E (600, 699): {contadorE} \n" +
        f"Intervalo F (700, 799): {contadorF} \n" +
        f"Intervalo G (800, 899): {contadorG} \n" +
        f"Intervalo H (900, 999): {contadorH} \n" +
        f"Intervalo I (1000, 9999): {contadorI} \n")    
    

comissao()