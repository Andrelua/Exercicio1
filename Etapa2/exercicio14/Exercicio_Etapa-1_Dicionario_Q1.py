'''Uma biblioteca deseja fazer um sistema para alugar livro onde 
receba o nome da pessoa que ira alugar, a quantidade de dias
e o nome do livro, por fim exiba todas as informações. 
obs: utilize dicionario para guardar as informações.'''

clientes = {}


for i in range(1000):
    infor = []
    chave = input("Qual o nome do cliente? ")
    infor.append(int(input("Qual a quantidade de dias ?")))
    infor.append(input("Qual o nome do livro ?"))
    valor = infor
    clientes[chave] = valor
    exit = input("Deseja encerrar (Y/N)?")
    if exit == "Y":
        break

print("INFORMAÇÕES: ")
for chave, valor in clientes.items():
    print(f"NOME: {chave} \nDIAS: {valor[0]} \nNOME: {valor[1]}.")
    print("-" * 10)