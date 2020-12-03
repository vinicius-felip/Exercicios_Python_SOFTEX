import unidecode
from os import system

def exibirPalavrasPali(*lista):
    for palavra in lista[0]:
        if verifPali(palavra):
            print (verifPali(palavra))
            
def verifPali(palavraOriginal):
    palavraInversa = str()
    palavraPali = unidecode.unidecode(palavraOriginal).upper().split()
    palavraPali = ''.join(palavraPali)

    for i in range(len(palavraPali)-1,-1,-1):
        palavraInversa += palavraPali[i]

    if palavraInversa in palavraPali:
        return f'A palavra {palavraOriginal} é um palíndromo, pois ao contrário fica {palavraInversa}  '
        
palavrasPali = []

lista = []

system('cls')

loop = int(input('Quantas palavras você quer digitar? '))

for i in range(loop):
    lista.append(input('Digite uma palavra pra saber se é palíndromos: '))
    
system('cls')
exibirPalavrasPali(sorted(lista))