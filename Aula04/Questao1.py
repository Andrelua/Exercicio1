times = ('Sport Recife', 'Náutico', 'Santa Cruz', 'Salgueiro', 'Central', 'Afogados', 'Vitória', 'Petrolina', 'América', 'Flamengo Arc.')

print('-='* 15)
print(f'Primeiro colocado: {times[0]} \nSegundo colocado: {times[1]} \nTerceiro colocado: {times[2]}')
print('-='* 15)
print(f'Sétimo colocado: {times[-4]} \nOitavo colocado: {times[-3]} \nNono colocado: {times[-2]} \nDécimo colocado: {times[-1]}')
print('-='* 15)
print(sorted(times))
print('-='* 15)
print(f"O time Vitória está na {times.index('Vitória')}º posição.")
print('-='* 15)