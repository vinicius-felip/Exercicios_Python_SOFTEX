'''
Caio quer retirar todas as vogais das palavras mas não sabe como.
Crie um algoritmo (usando tuplas) que faça este trabalho para Caio.

Banana => BNN
Acerola => CRL

'''
import unidecode

vogais = ('A','E','I','O','U')

palavra = input("Digite a palavra: ")
palavraNova = str()

for letra in unidecode.unidecode(palavra):
    if not letra.upper() in vogais:
        palavraNova += letra

print('A nova palavra é: ', palavraNova)