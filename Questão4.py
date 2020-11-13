# Jogo da Forca: A palavra é adicionada pelo jogador e verifica se já escreveu uma letra.
# Para o sorteio usei o módulo random, que é um módulo builtins do próprio python.
import random as rd

print('=============================')
print('       JOGO DA FORCA')
print('=============================')

palavras = ['Coelho', 'Cachorro', 'Gato', 'Elefante', 'Baleia', 'Bola', 'Balao', 'Caderno', 'Python']
palavra_escolhida = rd.choice(palavras)
print('Regras: ')
print('Só há 10 chances de acertar;')
print('Informe a letra em maiústculo.')
print('Começamos o jogo: \n')

# Transformando o tamanho da palavra sorteada em traços.
tracos = list(len(palavra_escolhida) * '-')

# Imprimindo em formato de lista. 
print(list(tracos))
print('\n')

# Transformando a palavra sorteada em uma lista de letras maiúsculas.
lista_palavra = list(palavra_escolhida.upper())

"""# Convertendo os traços em lista.
tracos = list(tracos)"""

# O jogo verdadeiro, verificando se a letra consta na palavra, no caso lista. Adicionando a letra informada na posição 'i' da lista de traços,
# imprimindo a lista. Por último, verificando se a lista traços é igual a palavra sorteada transformada em lista, depois verifica se as chances 
# ja acabaram.
chances = 0
while chances <= 10:
    letra = input('Informe uma letra:')
    print('\n')
    for i in range(len(lista_palavra)):
        if letra.strip() == lista_palavra[i]:
            tracos[i] = letra
    print(tracos, '\n')
    if tracos == lista_palavra:
        print('Parabéns, você ganhou!!')
        break
    if chances == 10:
        print('Acabaram-se as chances e você perdeu !!')
    chances += 1
 