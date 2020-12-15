

def combustivel():
    carros = []
    for i in range(5):
        print(f'Veiculo {i+1}:')
        nome = input("Nome: ")
        kmL = float(input("Kms por litro: "))
        carros.append([nome, kmL])
    
    consumo = []
    litros = []
    for i in range(5):
        calculo1 = (1000 / carros[i][1])
        calculo2 = calculo1 * 4.93
        consumo.append(calculo2)
        litros.append(calculo1)
    print("Relatória Final")
    for i in range(5):
        print(f"{i+1} - {carros[i][0]} - {carros[i][1]} - {litros[i]:.2f} litros - R$ {consumo[i]:.2f}")

    menor = 9999999
    nome =  ''
    for i in range(5):
        if consumo[i] < menor:
            menor = consumo[i]
            nome = carros[i][0]
    print(f"\n O mais econômico é o {nome}")

combustivel()