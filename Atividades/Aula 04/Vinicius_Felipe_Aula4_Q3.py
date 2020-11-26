import random as rd
print ('------------------------------')
qtJogos = int(input("Quantos jogos serão gerados? "))
 
for i in range(qtJogos):   
    print ('Jogo', i+1, sorted(rd.sample(range(1,61),6)))
print ('------------------------------')