'''Um aluno deseja saber suas médias antes da postagem de seu professor
para planejar com antecedência as suas férias. O aluno deseja criar um 
sistema que receba os nomes das disciplinas ( no mínimo 5) e as médias. 
Se o aluno tiver média maior ou igual a 7 o aluno em todas as matérias 
cadastradas ele está de férias. Se alguma média for menor que 7 ele 
não estará de férias. Use lista e função padrão para criar seu programa. 
O seu programa deve mostrar a situação do aluno como resultando, 
exibindo se ele está de férias ou não.'''

import os
limpa = lambda: os.system('cls')

disciplinas = list()
notas = list()
def ferias():
    loop = True
    while loop:
        limpa()
        global disciplinas
        global notas
        resposta = str()
        disciplinas.append(input('\nDigite o nome da disciplina: '))
        notas.append(float(input(f'Digite a nota obtida na discplina: ')))
        if len(disciplinas) >4:
            while not resposta in ['S','N']:
                resposta = input('\nS - SIM\nN - Não\nDeseja continuar a adiconar disciplinas?').upper()
                print(resposta)
            if resposta in 'N':
                loop = False
                for nota in range(7):
                    limpa()
                    if nota in notas:
                        return 'não está de férias ;-;\n'
                    elif nota == 6:
                        return 'de férias \o/\n'
                                    
print(f'Você {ferias()}')
            

            
