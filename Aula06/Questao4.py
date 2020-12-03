"""Faça um programa que tenha uma função com parâmetro padrão que
dado o valor da conta de um restaurante, calcule e exiba a gorjeta do
garçom e o valor total da conta acrescentando essa gorjeta.
Esse programa também deve permitir o não pagamento da gorjeta.
"""


def pagamento(valor=0):
    if valor == 0:
        print(f"O valor da conta deu igual a: R$ {valor}")
    else:
        gorjeta = 0.1
        valor = valor + (valor * gorjeta)
        print(f"O valor da conta com a gorjeta deu igual a: R$ {valor}")

pagamento()
pagamento(1500)