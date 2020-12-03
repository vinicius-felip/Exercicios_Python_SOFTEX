from os import system
import random

def maior(*valores):
    print('Números gerados na lista: ', valores[0])
    if valores[0]:
        return f'Valor máximo: {max(valores[0])}\nValor mínimo: {min(valores[0])}\n'
    return f'Valor máximo: Não tem valor\nValor mínimo: Não tem valor\n'

system('cls')
print(maior((random.sample(range(0,10),random.randint(0,10)))))