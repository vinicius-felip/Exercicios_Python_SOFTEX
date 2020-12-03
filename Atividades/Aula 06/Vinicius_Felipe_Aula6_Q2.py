def contagem(i,f,p):
    for i in range(i,f,p):
        print(i)
        
print('-'*20)
print('Contagem de 1 até 10 passo 1: ')       
contagem(1,10+1,1)

print('-'*20)
print('Contagem de 10 até 0 passo -2: ')       
contagem(10,0-1,-2)

print('-'*20)
print('Escolha a próxima contagem')

inicio = int(input('de '))
fim = int(input('até '))
passo = int(input('passo '))  

print('-'*20)
print(f'Contagem de {inicio} até {fim} passo {passo}:')
contagem(inicio,fim,passo)
