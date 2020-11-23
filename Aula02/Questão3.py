"""Calcular a média final e a situação de um aluno seguindo as seguintes condições: 3 provas
e obrigação de no mínimo 75% de freqüência. Serão fornecidos pelo usuário as notas das
três provas e o percentual de freqüência de cada aluno. Com estas informações fornecidas
apresentar a média final do aluno e a sua situação – aprovado ou reprovado. Média para
aprovação maior ou igual a 7.0."""

notas = []
for i in range(3):
    notas.append(float(input(f'Informe a nota da prova: ')))
med = sum(notas)/3

frequencia = float(input('Qual o percentual de frequência? '))

if (frequencia >= 75.0) and (med >= 7.0):
    print(f'O aluno foi aprovado !!, com média: {med} e {frequencia}% de percentual de frequência.')
else:
    print(f'O aluno foi reprovado !!, com média: {med} e {frequencia}% de percentual de frequência.')

