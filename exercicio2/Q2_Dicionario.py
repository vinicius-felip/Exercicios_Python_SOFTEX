'''
Utilizando o dicionário:
{'Brasil': 5, 'Alemanha': 4, 'Itália': 4, 'França': 2, 'Argentina': 'Espanha': 1, 'Inglaterra': 1, 'Uruguai': 1}
Onde contem as seleções campeãs mundiais e a quantidade de vezes que ganharam a Copa do Mundo.
Faça um algoritmo que peça uma seleção e seja exibida a quantidade de vezes que ela foi campeã.
Ao final, pergunte se o usuário quer verificar outra seleção, se sim pergunte a seleleção novamente
exiba o novo resultado.  
'''

selecoes = {'Brasil': 5, 'Alemanha': 4, 'Itália': 4, 'França': 2, 'Argentina':1, 'Espanha': 1, 'Inglaterra': 1, 'Uruguai': 1}
loop = True
while loop:
    print('-'*20)
    for selecao in selecoes:
        print(selecao)
    print('-'*20)

    loopEscolha = True
    while loopEscolha:
        escolhaSelecao = input('Escolha uma seleção: ').capitalize()
        if escolhaSelecao in selecoes:
            print(f'\nA seleção do/da {escolhaSelecao} ganhou {selecoes[escolhaSelecao]} copa do mundo. ')
            loopEscolha = False
        else:
            print('Erro de digitação ou Seleção não faz parte da lista.')
            
    if 1 == int(input('Você deseja repetir?\n1 para NÃO\nOu Qualquer número para SIM\n')):
        loop = False

        