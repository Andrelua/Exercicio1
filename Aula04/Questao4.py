quantidade = int(input('Quantos alunos nós temos ? '))
alunos_n = []
alunos_notas = []
for i in range(0,quantidade):
    nome_aluno = input('Nome: ')
    nota1 = int(input('Nota 1: '))
    nota2 = int(input('Nota 2: '))
    alunos_n.append(nome_aluno)
    alunos_notas.append([nota1, nota2])

med = []
for i in range(0, quantidade):
    med.append(sum(alunos_notas[i])/2)

print('No.  Nome  Média')  
print('-'*18)
for i in range(0, quantidade): 
    print(f'{i}   {alunos_n[i]}   {med[i]}')

print('-'*18)

encerrar = False
while encerrar == False:
    i = int(input('Mostrar notas de qual aluno ? (999 imterrompe): '))
    if i == 999:
        print("ATÉ PRÓXIMA !!!")
        encerrar = True
    else:
        print(f'As notas de {alunos_n[i]}: {alunos_notas[i]}')