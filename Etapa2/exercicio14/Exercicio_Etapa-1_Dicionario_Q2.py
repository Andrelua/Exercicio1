'''Faça um sistema de cadastro de entrada dos pacientes no hospital,
utilizando dicionario guarde as informações do nome
e se o estado do paciente é (Leve, Grave ou Critico). 
Se o paciente estiver em estado leve recebera a pulseira verde, 
grave amarela e critico vermelha, por fim exiba todos os
pacientes cadastrados e tambem exiba os paciente de maneira
separada pela sua pulseira.'''
pacientes = {}
verde = []
amarelo = []
vermelha = []

for i in range(1000):
    chave = input("Qual o nome do paciente? ")
    valor = input("Qual o estado dele (Verde, Amarelo, Vermelho)? ")
    pacientes[chave] = valor
    exit = input("Deseja encerrar (Y/N)? ")
    if exit == "Y":
        break

for chave, valor in pacientes.items():
    if valor == "Verde":
        verde.append(chave)
    elif valor == "Amarelo":
        amarelo.append(chave)
    else:
        vermelha.append(chave)

print("PACIENTES EM ESTADO LEVE: ")
for i in range(0, len(verde)):
    print(f"Nome: {verde[i]}.")

print("PACIENTE EM ESTADO GRAVE: ")
for i in range(0, len(amarelo)):
    print(f"Nome: {amarelo[i]}.")

print("PACIENTE EM ESTADO CRÍTICO: ")
for i in range(0, len(vermelha)):
    print(f"Nome: {vermelha[i]}.")