# Com os meses do ano e seus respectivos dias faça:
# Mostre os meses com 31 dias.
# Mostre os meses com 30 dias.
# Utilize dicionário.


meses = {'Jan': 31, 'Fev': 29, 'Mar': 31, 'Abr': 30, 'Mai': 31, 'Jun': 30, 'Jul': 31, 'Ago': 31, 'Set': 30, 'Out': 31, 'Nov': 30, 'Dez': 31}

print('Meses com 31 dias.')
for chave, valor in meses.items():
    if valor == 31:
        print(f'{chave} {valor} dias')

print('Meses com 30 dias.')
for chave, valor in meses.items():
    if valor == 30:
        print(f'{chave} {valor} dias')

print('Meses com menos de 30 dias.')
for chave, valor in meses.items():
    if valor < 30:
        print(f'{chave} {valor} dias')