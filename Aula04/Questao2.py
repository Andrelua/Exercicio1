lista = ('Mouse', 120.00, 'Teclado', 150.00, 'Monitor', 650.00)

print('Listagem de preços: ')
for i in range(0, len(lista), 2): 
    print(f'{lista[i]}........... R$ {lista[i+1]}')
