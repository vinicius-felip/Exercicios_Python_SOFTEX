import random       
from collections import defaultdict
from os import system
from time import sleep

system('cls')
jogadores = (1,2,3,4)
dados = []
jogo = dict(Jogador = jogadores, Dados = dados)

loop = True

while loop == True:
    system('cls')
    print('Valores sorteados:')
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")


    for i in range(len(jogadores)):
        dados.append(random.choice(range(1,7)))
        print ('Jogador {0} tirou {1} no dado'.format(jogo['Jogador'][i],dados[i]))
        sleep(0.5)
    print('_________________________\n')



    verificacao = defaultdict(list)
    for chave, valor in enumerate(dados):
        verificacao[valor].append(chave)
        
  
    if not  (len(verificacao))>3:
        print ('Ocorreu um empate')
        sleep(1.0)
        dados = []
    else:
        loop = False

        
        
#RESULTADO        
print('Ranking do Jogadores:') 
print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")       
posicao = 1
for i in range(6,0,-1):
    for k in range(len(dados)):
        if i == dados[k]:
            print ('{}º lugar: Jogador {} com {} '.format(posicao,jogadores[k], i))
            posicao += 1
print('_________________________') 