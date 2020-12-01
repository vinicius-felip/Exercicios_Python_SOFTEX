'''
João quer organizar sua lista de compras em ordem alfábetica, mas não sabe como.
Crie um algoritmo (usando dicionario) para ajudar joão com sua lista de compras, 
sabendo que a ordem da lista atual é: {'Feijão': 5.50: 'Arroz': 4.75: 'Macarrão': 3.10: 'Leite': 6.45: 'Ovos': 9.20}

Feijão      R$ 5,50 
Arroz       R$ 4,75
Macarrão    R$ 3,10
Leite       R$ 6,45
Ovos        R$ 9,20
--------------------
Total       R$ 29.00

No final exiba o valor total de compras

'''
print ('-'*23)

compras = {'Feijão': 5.50, 'Arroz': 4.75, 'Macarrão': 3.10, 'Leite': 6.45, 'Ovos': 9.20}

for dados in sorted(compras.items()):
    print ('{:<10}\tR$ {:.2f}'.format(dados[0],dados[1]))

print ('-'*23)
print (f'Total\t\tR$ {sum(compras.values()):}')

