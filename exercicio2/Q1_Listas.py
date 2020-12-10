'''
Faça um jogo de par ou ímpar, dividindo os números de 0 a 100 
em 2 listas: ímpares e pares. Onde o jogador digita um número e 
é exibido se o número digitado é ímpar ou par.
(USE LISTAS)
'''
par = list(range(0,101,2))
impar = list(range(1,100,2))

numEscolhido = int(input('Qual número você vai escolher entre 0 e 100? '))

if numEscolhido in par:
    print('O número escolhido é par!')
elif numEscolhido in impar:
    print('O número escolhido é impar!')
else:
    print('O número escolhido não está entre 0 e 100.')