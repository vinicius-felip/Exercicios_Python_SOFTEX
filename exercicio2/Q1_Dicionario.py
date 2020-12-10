'''
A professora quer saber quem é o mais alto, o mais baixo e a 
média de alunos de uma turma de 10 alunos.
Faça um algoritmo que ajude ela com esses dados, usando dicionário. 
Onde as chaves sejam os de cada e os valores as alturas.

'''
altura = dict()

for numAluno in range(10):
    altura[input('Qual o nome do aluno? ')] = float(input(f'Qual é a altura de ? '))

print(f'O aluno mais alto é {max(altura,key=altura.get)} com {max(altura.values())}m ')
print(f'O aluno mais baixo é {min(altura,key=altura.get)} com {min(altura.values())}m ')
print(f'A média da altura da turma é de {(sum(altura.values()))/10}m')
