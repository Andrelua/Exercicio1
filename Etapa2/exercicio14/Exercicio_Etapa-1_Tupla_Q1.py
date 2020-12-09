'''Uma familia formada pelo pai(Antonio), Mãe(Maria), filho(Caio), 
filha(Bia) estão com um pequeno problema para decidir
quem na semana ira ficar responsavel por lavar a louça e encher as
garrafas de água da geladeira, então faça um programa
usando "tupla" para sortear quem ira ficar com cada função, 
lembrando que a mesma pessoa não pode ficar com as duas
funções e a filha(bia) não pode lavar a louça porque só tem 9 anos.'''
import random as rd

familia = ("Bia", "Antonio", "Maria", "Caio")

i = rd.randint(0, 3)
j = rd.randint(1,3)

print(f"Quem vai lavar a louça é: {familia[i]}.")

if familia[i] == familia[j]:
    print(f"E quem também vai encher as garrafas de água da geladeira é {familia[j]}.")
else:
    print(f"E quem vai encher as garrafas de água da geladeira é {familia[j]}.")
