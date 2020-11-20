def verificarResultado (x,y):
    if (x == 0 and y == 2):
        result = 1
    elif (y == 0 and x == 2):
        result = 2       
    elif (x > y):
        result = 1
    elif (y > x):
        result = 2
    elif (x == y):
        result = 0
    return result

player1 = input("\nDigite o nome do Player 1\n")
player2 = input("Digite o nome do Player 2\n")

loop = True
rodadas = 0
vitoriasP1 = 0
vitoriasP2 = 0

while (loop == True):
    print("_____________________________________")
    print ("\nEscolha uma das alternativas:")
    print ("0 - PAPEL:")
    print ("1 - TESOURA:")
    print ("2 - PEDRA:\n")
    jogadaPlayer1 = int(input("Player 1: "))
    jogadaPlayer2 = int(input("Player 2: "))

    resultado = verificarResultado(jogadaPlayer1,jogadaPlayer2)
    
    if (resultado == 1):
        vitoriasP1 += 1
        rodadas += 1
    elif (resultado == 2):
        vitoriasP2 += 1 
        rodadas += 1
    else:
        rodadas += 1
    if (rodadas>1 and (vitoriasP1>vitoriasP2 or vitoriasP2>vitoriasP1)):
        loop  = False

print("_____________________________________")   
     
if (vitoriasP1>vitoriasP2):
    print ("{} venceu por {} à {} com o total de {} rodadas" .format(player1, vitoriasP1, vitoriasP2, rodadas))
else:
    print ("{} venceu por {} à {} com o total de {} rodadas" .format(player2, vitoriasP2, vitoriasP1, rodadas))
        





