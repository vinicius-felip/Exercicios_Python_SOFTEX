'''
Faça uma pesquisa com 10 pessoas, onde elas terão que informar 
seu time preferido de Pernambuco. 
Depois exiba um ranking com o top 3 favoritos da galera. 
Exiba também o numero de votos de cada time. 
Em caso de empate refaça a pesquisa, até desempatar.
(USE TUPLAS)
'''

from time import sleep
from os import system

loopVotos = True
while loopVotos:
    system('cls')
    times = ('Sport','Santa cruz', 'Náutico', 'Ibis', 'Salgueiro', 'Central')
    times_Votacao = dict()

    print('-'*20)
    for time in times:
        times_Votacao[time] = int()
        print(time)          
    print('-'*20)

    while sum(times_Votacao.values())<10:        
        loop = True
        while loop:
            voto = input('Escolha um time: ').capitalize()
            if voto in times:
                times_Votacao[voto]+= 1
                loop = False
            else:
                print('Erro de digitação ou time não faz parte da lista.')
            

    ranking_Times = sorted(times_Votacao,key=times_Votacao.get,reverse=True)[:3]


    print('-'*20)
    print('Raking dos 3 times mais votados\n')
    print(f'Nome\t\tVotos\n')
    for posicao in range(len(ranking_Times)):
        print(f'{posicao+1:<2}{ranking_Times[posicao]:<17}{times_Votacao[ranking_Times[posicao]]}')
    print('-'*20)
    
    if times_Votacao[ranking_Times[0]] == times_Votacao[ranking_Times[1]] == times_Votacao[ranking_Times[2]]:
        print("Houve um empate entre os 3 primeiros colocados! Iremos refazer a votação.")
        sleep(5)
    else:
        loopVotos = False
        