'''5 amigos decidem se reunir para assistir um filme na casa de um 
deles entre o horario das 15:00 ate 22:00 horas,
mas cada um deles quer assistir um filme diferente que são;
(O Poço, Sementes Podres, Bacurau, Corra, Um Lugar Silencioso),
faça um sorteio utilizando tupla para decidir o filme, 
porém se eles decidirem assistir o filme depois das 18:00 horas
só poderão assistir os filmes de terror que são 
(Corra ou Um Lugar Silencioso).'''

import random as rd

filmes = ("O Poço", "Sementes Podres", "Bacurau", "Corra", "Um Lugar Silencioso")
filmes18 = ("Corra", "Um Lugar Silencioso")

horario = float(input("Em que horário irão assistir o filme (EX: 18.30): "))

i = 0
if horario < 18:
    i = rd.randint(0,4)
    print(f"Vamos assitir o filme {filmes[i]}")
else:
    i = rd.randint(0,1)
    print(f"Vamos assitir o filme {filmes18[i]}")