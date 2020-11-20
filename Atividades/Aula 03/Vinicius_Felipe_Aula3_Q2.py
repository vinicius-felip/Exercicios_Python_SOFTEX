import os
import time

def exibirQuadrado():
    
    print("*  " * 5)
    for i in range(3):
        print ("*",end=" ")
        for j in range(4):
            if j == 3:
                print(" *")
            else:
                print (" {} ".format(quad[i][j]), end="")
    print("*  " * 5)
    

def verifLados():
    somalados = []
    resultHoriz = 0
    resultVerti = 0
    resultDiagE = 0
    resultDiagD = 0
    posicao = 2
    for i in range(3):
        resultHoriz = 0
        resultVerti = 0
        for j in range(3):
            resultHoriz += quad[i][j]
            resultVerti += quad[j][i]
            if i == j:  
                resultDiagE += quad[i][j]
            if j == posicao:   
                resultDiagD += quad[i][j]
                posicao -= 1 
        somalados.append(resultHoriz) 
        somalados.append(resultVerti) 
    somalados.append(resultDiagE)
    somalados.append(resultDiagD)
    
    result = 0
    for i in range(8):
        if somalados[i] == somalados[0]:
            result += 1
    if result == 8:
        return True
    else:
        return False
           
def main():
    
    entrada = [0,1,2,3,4,5,6,7,8,9]
    for i in range(3):
        for j in range(3):
            quad[i].append("_") 

    for i in range(3):
        for j in range(3):
            loop = True
            while loop == True:
                os.system("cls")
                exibirQuadrado()
                pergunta = int(input("Digite o valor de 0 à 9 para adicionar ao quadrado 3x3 na linha {}, coluna {}: ".format(i+1, j+1)))
                if pergunta in entrada:
                    quad[i][j] = pergunta
                    loop = False
                else:
                    print ("Valor não válido") 
                    time.sleep(0.7)
    loop = True
    while loop == True: 
        os.system("cls")
        exibirQuadrado()
        print ("\nDeseja saber se o quadrado é mágico?")
        pergunta = int(input("0 - Sim\n1 - Não\n"))
        if pergunta == 0:
            loop = False
            os.system("cls")
            exibirQuadrado()
            if verifLados():
                print("\nQuadrado é mágico\n")
            elif not verifLados():
                print("\nQuadrado não é mágico\n")
        elif pergunta == 1:
            loop = False
            print ("Tenha um bom dia!")
        else:
            print ("Valor não válido") 
            time.sleep(0.7) 
                
                
                
            
        
 
    










quad = [[],[],[]]        
main()

            
    
           