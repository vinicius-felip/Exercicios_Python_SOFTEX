from os import system

system('cls')

gols = []
info = dict(Nome = str(), Gols = gols, Total = int())

info['Nome'] = input('Nome do jogador: ')
jogos = int(input('Quantas partidas {} jogou? '.format(info['Nome'])))

for i in range(jogos):
    gols.append(int(input(f'Quanto gols na partida {i+1}: ')))    

info['Total'] = sum(info['Gols'])

print('\n‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
print(info)

print('\n‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')

print('O campo nome tem o valor {}.'.format(info['Nome']))
print('O campo gols tem o valor {}.'.format(info['Gols']))
print('O campo total tem o valor {}.'.format(info['Total']))

print('\n‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')

print('O jogador {} jogou {} partidas.'.format(info['Nome'], jogos))
for partida in range(jogos):
    print('     --> Na partida {}, fez {} gols.'.format(partida+1,info['Gols'][partida]))
    