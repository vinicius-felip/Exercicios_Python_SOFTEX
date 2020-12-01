'''
Larissa quer saber a quantidades de vogais em uma palavra.
Crie um algoritmo (usando tuplas) que faça este trabalho para Larissa.

'''
import unidecode

vogais = ('A','E','I','O','U')

palavra = input("Digite a palavra: ")
cont = 0

for letra in unidecode.unidecode(palavra):
    if letra.upper() in vogais:
        cont += 1

print(f'\nA Palavra "{palavra}" possui {cont} vogais')