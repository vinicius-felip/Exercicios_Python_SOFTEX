'''
O técnico de um time quer saber a média de idade, o jogador mais velho e mais novo do seu clube,
além de uma tabela onde mostre a idade de todos os 15 atletas. Faça um algoritmo usando 2 listas,
uma para o nome e outra para a idade, que ajude o técnico com isso.
'''

nomeJogador = []
idadeJogador  = []

while len(nomeJogador)<15:
    nomeJogador.append(input('Qual o nome do jogador? '))
    idadeJogador.append(int(input('Qual a idade do jogador? ')))
    

print('-'*15)
print(f'Nome\t\tIdade\n')
for dadosJogador in range(len(nomeJogador)):
    print(f'{nomeJogador[dadosJogador]:<17} {idadeJogador[dadosJogador]}')          
print('-'*20)

print(f'\nO Jogador mais velho é {nomeJogador[idadeJogador.index(max(idadeJogador))]} com {max(idadeJogador)} anos')
print(f'O Jogador mais novo é {nomeJogador[idadeJogador.index(min(idadeJogador))]} com {min(idadeJogador)} anos')
print(f'A média de idade dos Jogadores é {(sum(idadeJogador))/len(nomeJogador)} anos\n')