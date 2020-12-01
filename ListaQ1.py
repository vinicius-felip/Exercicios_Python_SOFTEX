'''
Maria é professora e quer escrever as duas notas de X alunos da sala de aula 
e depois saber a média do aluno que ela escolher. Crie um algoritmo 
(usando lista) que ajude Maria a executar essa tarefa.

Quantos alunos há na sala? 1
---------------
Digite o nome do Aluno: João
Digite a 1º nota do aluno: 7
Digite a 2º nota do aluno: 9
---------------
1   João       [7.0, 9.0]
---------------
De qual aluno deseja ver a média? 1
---------------
João tem média 8.0

'''



sala = int(input('Quantos alunos há na sala? '))
alun = []

for numAluno in range(sala):
    nota = []
    notas = []
    print ('-'*15)
    notas.append(input('Digite o nome do Aluno: '))
    for notaAluno in range(2):
        nota.append(float(input(f'Digite a {notaAluno+1}º nota do aluno: ')))
    notas.append(nota)    
    alun.append(notas)
print ('-'*15)

for numAluno in range(sala):
    print(f"{numAluno+1:<3} {alun[numAluno][0]:<10} {alun[numAluno][1]}" )

print ('-'*15)
escolhaMedia = int(input('De qual aluno deseja ver a média? '))
print ('-'*15)
print(f'{alun[escolhaMedia-1][0]} tem média {sum(alun[escolhaMedia-1][1])/2}')




