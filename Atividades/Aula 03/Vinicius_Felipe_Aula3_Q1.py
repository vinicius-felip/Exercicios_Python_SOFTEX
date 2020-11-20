import random
import os

os.system("cls")
def rolarDados():
    dado1 = random.randrange(1,7)
    dado2 = random.randrange(1,7)
    dados = dado1+dado2
    return dados
pontos = 0 
loop = True
while loop == True:
    jogar = int(input("Quer jogar?\n1 - Sim\n0 - Não\n"))
    if jogar == 1: 
        dados = rolarDados() 
        print("Você tirou ", dados)
        if dados in (7,11):   
            print('Você ganhou')
            loop = False
        elif dados in (2,3,12):
            print('Você perdeu')
            loop = False
        else:
            loop = True
            while loop == True:
                print('Seu número agora é {}, tire o mesmo número para pontuar ou 7 para perder e mostrar a pontuação. Boa sorte!'.format(dados))  
                jogar = int(input("Quer jogar?\n1 - Sim\n0 - Não\n"))
                if jogar == 1:
                    dados2 = rolarDados()
                    print("Você tirou ", dados2)
                    if dados2 == dados:
                        pontos += 1
                    elif dados2 == 7:
                        loop = False
                        print ("Você tirou 7 e Perdeu! Você fez {} pontos".format (pontos))  
                elif jogar == 0:
                    loop = False
                    print ("Você Perdeu! Você fez {} pontos".format (pontos)) 
                else:
                    print('Digite uma opção válida')
    elif jogar == 0:
        loop = False
        os.system("cls")
        print ("Tchau!") 
    else:
        print('Digite uma opção válida')
        os.system("cls")
                    

                    
                
