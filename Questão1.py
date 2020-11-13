# Ler dois números e retornar o dividendo, divisor, quociente e o resto da divisão.

numero1 = float(input('Me informe o primeiro número: '))
numero2 = float(input('Me informe o segundo número: '))

print(f'O dividendo da equação é o nº {numero1}.')
print(f'O divisor da equação é o nº {numero2}.')
print(f'O quociente da equação é {round((numero1 / numero2),2)}')
print(f'O resto da equação é {numero1 % 2}')

