import platform
import os
limpa = lambda: print('\n'*130)

path = str(os.path.abspath(''))
for caminho, diretorios, arquivos in os.walk('.'):
    if 'Itens_Feira.txt' in arquivos:
        path += str(caminho).replace('.','')+'\\' + str(arquivos[0])

arquivo = open(f'{path}', 'r', encoding= 'utf8')
produtos = arquivo.readlines()

notaFiscalFeita = False
carrinhoPython = list()
notafiscalPython = list()
notafiscalTxt = str()
totalCompra = list()
carrinhoPython.append('Nº   Produto                                                  Preço    Qnt     Preço Total')
carrinhoPython.append('-'*90)

escolhasProdutos = ('A','C','S','Q','P')
escolhasCarrinho = ('A','F', 'R','S')


pagina = 1



#FUNÇÕES RELACIONADAS A PAGINA ----------------------------------------------------------------------------


def dadosPagina(nPagina):
    print('\t\t\t\t PÁGINA')
    print(f'                             Q << {str(nPagina)} - 7 >> P')
    print('A = Adicionar um item\nC = Exibir Carrinho\nS = Sair da Feira\nQ = Página Anterior   \nP = Próxima Página\n')


def exibirProdutos():
    for linha in range(len(produtos)):
        if pagina == 1:
            if linha == 16:
                dadosPagina(pagina)
                break
            print(produtos[linha])   
        if pagina == 2:
            if linha == 8:
                dadosPagina(pagina)
                break
            print(produtos[linha+17])    
        if pagina == 3:
            if linha == 10:
                dadosPagina(pagina) 
                break
            print(produtos[linha+26])    
        if pagina == 4:
            if linha == 24: 
                dadosPagina(pagina)
                break
            print(produtos[linha+37])    
        if pagina == 5:
            if linha == 10: 
                dadosPagina(pagina)
                break
            print(produtos[linha+62])    
        if pagina == 6:
            if linha == 8: 
                dadosPagina(pagina)
                break
            print(produtos[linha+73])    
        if pagina == 7:
            if linha == 7: 
                dadosPagina(pagina)
                break
            print(produtos[linha+82]) 
            
            
    
            
#---------------------------------------------------------------------------------------------------------          

#FUNÇÕES RELACIONADAS A ADICIONAR PRODUTO NO CARRINHO ---------------------------------------------------------------------       
            
def adicionarProduto():
    numInexistente = True
    while numInexistente:
        numProduto = int(input('Número do produto: '))
        if pagina == 1 and numProduto in list(range(1,14)): 
            numInexistente = False
        if pagina == 2 and numProduto in list(range(1,6)):
            numInexistente = False
        if pagina == 3 and numProduto in list(range(1,8)):
            numInexistente = False
        if pagina == 4 and numProduto in list(range(1,22)):
            numInexistente = False
        if pagina == 5 and numProduto in list(range(1,8)):
            numInexistente = False
        if pagina == 6 and numProduto in list(range(1,6)):
            numInexistente = False
        if pagina == 7 and numProduto in list(range(1,5)):
            numInexistente = False          
    qntProduto = int(input('Quantidade (g/kg/ml): '))
    if pagina == 1:
        adicionarProdutoLinha(numProduto,qntProduto,2)
    if pagina == 2:
        adicionarProdutoLinha(numProduto,qntProduto,19)           
    if pagina == 3:
        adicionarProdutoLinha(numProduto,qntProduto,28)
    if pagina == 4:
        adicionarProdutoLinha(numProduto,qntProduto,39)
    if pagina == 5:
        adicionarProdutoLinha(numProduto,qntProduto,64)
    if pagina == 6:
        adicionarProdutoLinha(numProduto,qntProduto,75)
    if pagina == 7:
        adicionarProdutoLinha(numProduto,qntProduto,84)
 
 
def adicionarProdutoLinha(numProduto,qntProduto,linha):            
    valor = float(produtos[numProduto+linha][67:73].replace(',','.'))
    totalCompra.append(valor*qntProduto)
    carrinhoPython.append(f'{len(carrinhoPython)-1} - {produtos[numProduto+linha][5:62]}R$ {valor:.2f}\t{qntProduto}\tR$ {valor*qntProduto:->2,.2f}\n')   

#-----------------------------------------------------------------------------------------------------------

#FUNÇÕES RELACIONADAS AO CARRINHO--------------------------------------------------------------------------------


    



def exibirCarrinho():
    global totalCompra
    limpa()
    total = 'Total'
    dinheiro = 'R$'
    for linha in carrinhoPython:
        if carrinhoPython.index(linha)<2:
            print(linha)
        else:
            print(f'{carrinhoPython.index(linha)-1} {linha[2:]}')
    print('-'*90)
    print(f'{total:>88}\n{dinheiro:>83} {sum(totalCompra):.2f}')
    print('\nA = Adicionar outro item\nF = Finalizar compras\nR = Remover um produto\nS = Sair da Feira\n')
    escolhaCarrinho = None
    while not escolhaCarrinho in escolhasCarrinho:
        escolhaCarrinho = input('Qual ação você deseja realizar? ').upper()
        
    if escolhaCarrinho == 'A':#Adicionar outro produto
        acaoExibirProdutos()
        
    if escolhaCarrinho == 'F':#Finalizar Compras
        for linha in carrinhoPython:
            if carrinhoPython.index(linha)<2:
                notafiscalPython.append(linha+'\n')
            else:
                notafiscalPython.append(f'{carrinhoPython.index(linha)-1} {linha[2:]}')
        notafiscalPython.append('-'*90)
        notafiscalPython.append(f'\nTotal {dinheiro:>76} {sum(totalCompra):.2f}')
        finalizarCompras()
    
    if escolhaCarrinho == 'R':#Remover um produto
        produtoEscolhido = int()
        while not produtoEscolhido in list(range(1,len(totalCompra)+1)):
            produtoEscolhido = int(input('Número do produto:'))
        carrinhoPython.pop(produtoEscolhido+1)
        totalCompra.pop(produtoEscolhido-1)
        exibirCarrinho()
    
    if escolhaCarrinho == 'S':#Sair
        sair()
         
         
#FUNÇÃO RELACIONADA A FINALIZAR COMPRAS-------------------------------------------------------


def finalizarCompras():
    global notaFiscalFeita
    global notafiscalTxt
    limpa()
    formaPagam = int()
    print('FORMA DE PAGAMENTO\n1 - Cartão de Crédito/Débito\n2 - Dinheiro\n')
    while not formaPagam in list(range(1,3)):
        formaPagam = int(input('Qual forma de pagamento você deseja? '))
    if formaPagam == 1:
        notafiscalPython.append(f'\n\nForma de Pagamento: Cartão de Crédito')
    else:
        notafiscalPython.append(f'\n\nForma de Pagamento: Dinheiro')
    nome = input('Digite  seu nome completo: ')
    notafiscalPython.append(f'\nNome: {nome}')
    endereco = input('Digite seu endereço completo: ')
    notafiscalPython.append(f'\nEndereço: {endereco}')
    
    for linha in notafiscalPython:
        notafiscalTxt += linha
    
    caminho = os.path.expanduser('~')   
    
    sistemaOper = int(platform.release())
    
    if  sistemaOper == 10:
        notaFiscal = open(f'{caminho}\\OneDrive\\Área de Trabalho\\NotaFiscal_{nome}.txt','x+', encoding='utf8')
    else:
        notaFiscal = open(f'{caminho}\\Desktop\\NotaFiscal_{nome}.txt','x+', encoding='utf8')
    notaFiscal.write(str(notafiscalTxt))
    notaFiscalFeita = True
    sair()
        
    
    
    





















def acaoExibirProdutos():
    global pagina
    loop = True
    while loop:
        escolha = None
        limpa()
        exibirProdutos()
        while not escolha in escolhasProdutos:
            escolha = input('Qual ação você deseja realizar? ').upper()
        if escolha == 'A':#Adicionar produto
            adicionarProduto()
            
        if escolha == 'C':#Carrinho
            loop = False
            exibirCarrinho()

            
        if escolha == 'S':#Sair
            loop = False
            sair()
            
        if escolha == 'Q':#Voltar a página
            if not pagina == 1:
                pagina -= 1
            else:
                pagina = 7
        if escolha == 'P':#Pular de páagina
            if not pagina == 7:
                pagina += 1
            else:
                pagina = 1    
            

    
def sair():
    limpa()
    print('-='*25)
    print('Volte Sempre\n')
    if notaFiscalFeita:
        print('Sua nota fiscal foi enviada para a Área de Trabalho\n')
    
    

def menu():
    loop = True
    escolha = int()
    while loop:
        limpa()
        print('-='*25)
        escolha = int(input('\n1 - Entrar\n2 - Sair\n\nEscolha: '))
        if escolha == 1:
            loop = False
            acaoExibirProdutos()
        elif escolha == 2:
            loop = False
            sair()
        else: 
            print('\nOpção Inválida')
            
menu()
