'''
Ruana adicionou sem querer o mesmo item 2x na lista de compras e agora quer remover
e adicionar "Biscoito" no lugar . Crie um algoritmo (usando lista) que ajude
Ruana com o seu problema.

Feijão      
Arroz     
Macarrão
Macarrão    
Leite      
Ovos 
      
'''


lista = ['Feijão', 'Arroz', 'Macarrão', 'Macarrão', 'Leite', 'Ovos']
print(lista)
lista.remove('Macarrão')
lista.insert(2,'Biscoito')
print(lista)

