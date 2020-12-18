'''
Faça um sistema de cadastro de entrada dos pacientes no hospital, 
utilizando dicionário guarde as informações do nome, 
o estado do paciente é (Leve, Grave ou Critico). 
Se o paciente estiver em estado leve receberá a pulseira verde, 
se estiver em estado grave receberá a pulseira amarela e em estado 
crítico receberá a pulseira vermelha, por fim exiba todos os pacientes cadastrados, 
o seu estado e qual pulseira ele receberá. 
Para seu programa use pelo menos duas funções.
'''


def cadastrarPaciente(qntPacientes):
    global pacientes
    while not len(pacientes) == qntPacientes:
        nome = input('\nDigite o nome do paciente: ')
        pacientes[nome] = str()
        while not pacientes[nome] in ['Leve','Grave','Critico']:
            pacientes[nome] = input("-Leve\n-Grave\n-Critico\n\nDigite o estado do paciente: ").capitalize()
    exibirPacientes()
    
    
def exibirPacientes():
    print(f'\nPaciente       Situação ')   
    for nomePa, estado in pacientes.items():
        print(f'{nomePa:<18}{estado}')
        
pacientes = dict()

qntPacientes = int(input('Quantos pacientes você deseja cadastra: '))

cadastrarPaciente(qntPacientes)

