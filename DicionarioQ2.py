'''
Pedro quer mostrar para o seu chefe a lista dos setores que mais gastaram na 
empresa na ordem do mais alto para o mais baixo, mas não sabe como.
Crie um algoritmo (usando dicionario) para ajudar Pedro com sua lista, sabendo 
que a ordem da lista atual é: {'Administrativo': 10980.00, 'Financeiro': 4860.00, 'Recursos Humanos': 7090.00, 'Comercial': 6500.00, 'Operacional': 15500.00}

Administrativo          R$ 10980.00
Financeiro              R$  4860.00
Recursos Humanos        R$  7090.00
Comercial               R$  6500.00
Operacional             R$ 15500.00
--------------------
Total       R$ 29.00

No final exiba o valor total de compras

'''


compras = {'Administrativo': 10980.00, 'Financeiro': 4860.00, 'Recursos Humanos': 7090.00, 'Comercial': 6500.00, 'Operacional': 15500.00}
    
print ('-'*35)

for produto in sorted(compras, key =compras.get, reverse=True):
    print ('{:<16}\tR$ {:>8.2f}'.format(produto,compras[produto]))

print ('-'*35)
print (f'Total\t\t\tR$ {sum(compras.values()):.2f}')
