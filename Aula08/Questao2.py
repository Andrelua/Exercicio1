"""
Faça um programa que permite cadastrar pessoas com os seguintes
dados: nome e idade. Grave esses dados em um arquivo de txt.
O sistema ainda terá opção de cadastrar um nova pessoa e de listar as
pessoas que estão gravadas no arquivo.
Ao cadastrar uma nova pessoa, não deve apagar os registros
anteriores.
"""

# Não consegui fazer

with open('Cadastro.txt', 'a') as arquivo:
    while True:
        print("------- Cadastro -------")
        resposta = int(input("Opção: \n1 - Cadastrar \n2 - Listar \n0 - Sair\n"))
        
        if resposta == 1:
            nome = input("Nome: ")
            idade = input("Idade: ")
            arquivo.write(f"Nome: {nome} / Idade: {idade}.\n")
        elif resposta == 2:
            arquivo = open('Cadastro.txt', 'r')
            for line in arquivo:
                print(line)
        else:
            arquivo.close()
            break
        

    