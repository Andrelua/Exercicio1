# Converta as seguintes temperaturas de C° para F°: 
# Paris = 5°
# Recife = 26°
# Hong Kong = 16°
# Nova Iorque = 9°
# Barcelona = 15°
# Tóquio = 11°
# Egito = 14°
# Roma = 13°
# Utilize dicionário

paises = {'Paris': 51, 'Recife': 26, 'Hong Kong': 16, 'Nova Iorque': 9, 'Barcelona': 15, 'Tóquio': 11, 'Egito': 14, 'Roma': 13}

for chave, valor in paises.items():
    print(f'{chave} com {(valor * 9/5) + 32 } F°')