# Leia 10 valores e mostre a posição do maior e do menor no vetor. Use lista.

numeros = []
for i in range(0, 10):
    numeros.append(int(input(f'Informe o {i+1}º valor: ')))

print('\n')
print(numeros)  
print('\n') 

maior = 0
for i in range(0, 10):
    if (numeros[i] > maior):
        maior = numeros[i]
    
menor = 9999999999
for i in range(0, 10):
    if (numeros[i] < menor):
        menor = numeros[i]

print(f"A posição do maior número está na {numeros.index(maior)+1}º posição.")
print(f"A posiçao do menor número está na {numeros.index(menor)+1}º posição. ")