import random
from os import system
from time import sleep

escolhas = ('Papel', 'Tesoura', 'Pedra')
opcao = None

def verifVencedor(escolhaJogador):
    escolhaIA = random.choice(range(3))
    print(f'Você escolheu: {escolhas[escolhaJogador]}')
    print(f'A IA escolheu: {escolhas[escolhaIA]}\n')
    sleep(1.2)
    if (escolhaJogador == 0 and escolhaIA == 2):
        return f'O Jogador ganhou com {escolhas[escolhaJogador]} vs {escolhas[escolhaIA]}'
    
    elif (escolhaIA == 0 and escolhaJogador == 2):
        return f'A IA ganhou com {escolhas[escolhaIA]} vs {escolhas[escolhaJogador]}'       
    
    elif (escolhaJogador > escolhaIA):
        return f'O Jogador ganhou com {escolhas[escolhaJogador]} vs {escolhas[escolhaIA]}'
    
    elif (escolhaIA > escolhaJogador):
        return f'A IA ganhou com {escolhas[escolhaIA]} vs {escolhas[escolhaJogador]}'
    
    elif (escolhaJogador == escolhaIA):
        return f'Houve um empate com {escolhas[escolhaJogador]} vs {escolhas[escolhaIA]}'

while not opcao in range(3):
    system('cls')
    print("_____________________________________")
    print ("\nEscolha uma das alternativas:")
    print ("0 - PAPEL:")
    print ("1 - TESOURA:")
    print ("2 - PEDRA:\n")
    opcao = int(input())        
system('cls')
print(verifVencedor(opcao))







    