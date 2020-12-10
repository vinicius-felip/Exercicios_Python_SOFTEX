'''
Separe os 12 signos em 4 tuplas:
* Signos de Fogo - Áries, Leão e Sagitário.
* Signos de Terra - Touro, Virgem e Capricórnio.
* Signos de Ar - Gêmeos, Libra e Aquário.
* Signos de Água - Câncer, Escorpião e Peixes.
Depois peça para o usuário digitar um signo e em seguida informe de qual elemento é esse signo.
'''
fogo = ('Áries', 'Leão','Sagitário')
terra = ('Touro', 'Virgem' , 'Capricórnio')
ar = ('Gêmeos', 'Libra' , 'Aquário')
agua = ('Câncer', 'Escorpião' , 'Peixes')

loopEscolha = True
while loopEscolha:
    escolhaSigno = input('Digite um signo: ').capitalize()
    if escolhaSigno in fogo:
        print(f'{escolhaSigno} faz parte dos Signos de Fogo')
        loopEscolha = False
    elif escolhaSigno in terra:
        print(f'{escolhaSigno} faz parte dos Signos de Terra')
        loopEscolha = False
    elif escolhaSigno in ar:
        print(f'{escolhaSigno} faz parte dos Signos de Ar')
        loopEscolha = False
    elif escolhaSigno in agua:
        print(f'{escolhaSigno} faz parte dos Signos de Água')
        loopEscolha = False
    else:
        print('Erro de digitação ou Signo inexistente.')