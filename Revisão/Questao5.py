import random as rd

def embaralhar(string):
    a = list(string)
    rd.shuffle(a)
    palavra = "".join(a)
    print(palavra.upper())

embaralhar("André")