# Leia um vetor de 10 posições e verifique se o número digitado ja foi armazenado, se sim, leia novamente. No final mostre todos os números. 
# Use lista.

num = []
for i in range(0, 10):
    while True:
        if len(num) == 10:
            break
        num2 = int(input('Informe o número: '))
        if num2 not in num:
            num.append(num2)
        else:
            print('Este número ja está armazenado.')
            num2 = int(input('Armazene outro número: '))
        
                

print(num)
