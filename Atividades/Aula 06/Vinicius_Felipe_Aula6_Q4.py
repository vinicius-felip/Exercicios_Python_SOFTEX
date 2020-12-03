def valorGorjeta(valorconta, pagarGorj ,taxa = 0.12):
    if pagarGorj == 'S':
        return valorconta*taxa
    return 0

valid = ('S','N')
pagar = None

print('-'*20)
conta = float(input('Digite o valor da conta: R$ '))

while not pagar in valid:
    pagar = input('Você deseja pagar a gorjeta? [S/N] ').upper()
    
print(f'\nValor da gorjeta é: R$ {valorGorjeta(conta,pagar)}')
print(f'Valor total da conta é {valorGorjeta(conta,pagar)+conta}')