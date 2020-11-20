print('*********************************')
print('*** Jogo da Forca!***')
print('*********************************')
palavra_secreta = input("Escreva uma palavra para a forca: ")
letras_acertadas = []
for i in palavra_secreta:
    letras_acertadas.append('_')
    
enforcou = False
acertou = False
erros = 0
print(letras_acertadas)
alfa = []
i = 0
while(not enforcou and not acertou):
    valid = False
    while (valid == False):
        valid = True
        t = len(alfa)
        chute = input("Qual letra? ")
        if (not t == 0):
            for i in range(t):
                if (chute == alfa[i]):
                    print ("letra digitada")
                    valid = False
                    break
                else:
                    if (i == t-1):
                        alfa.append(chute)
        else: 
            alfa.append(chute)   
    if(chute in palavra_secreta):
        posicao = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_acertadas[posicao] = letra
            posicao = posicao + 1
    else:
        erros += 1
    enforcou = erros == 6  # teste lógico
    acertou = '_' not in letras_acertadas
    print(letras_acertadas)
if(acertou):
    print('Você ganhou!!')
else:
    print('Você perdeu!!')
print('Fim do jogo')