"""5. Faça um programa que possui uma função para verificar se n palavras
são palíndromos (é toda palavra ou frase que pode ser lida de trás pra
frente e que, independente da direção, mantém o seu sentido).
Essa função tem como parâmetro uma lista desses nomes que serão
inseridos através da digitação.
Ao final do programa deve-se exibir apenas as palavras palíndromos na
lista.
A lista não pode ter palavras iguais e deve ser ordenada por ordem
alfabética"""

def palindromo(*lista):
    for i in range(0,len(lista)):
        if (lista[i] == lista[i][::-1]):
            print(f"A palavra {lista[i]} é um palíndromo.")
        else:
            print(f"A palavra {lista[i]} não é um palíndromo.")


palindromo("andré", "arara", "cebola")
