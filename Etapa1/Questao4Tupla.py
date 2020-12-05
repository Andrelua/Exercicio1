#Dado determinados times, mostre os 5 primeiros, em ordem alfabética e os últimos 4. Utilize tupla.

times = ('Palmeiras', 'Sport', 'Náutico', 'Santana Cruz', 'São Paulo', 'Gremio', 'Salgueiro', 'ABC', 'BotaFogo', 'Atletico-MG')

print("# 5 primeiros")
for i in range(0, 5):
    print(times[i])

print('# Ordem alfabética')
print(sorted(times))

print('# Os últimos 4')
a = -4
for i in range(0, 4):
    print(times[a])
    a = a + 1