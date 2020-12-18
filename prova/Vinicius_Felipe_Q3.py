produtos = ('Arroz', 'Feijão', 'Macarrão', 'Biscoito', 'Bolacha', 'Cereal')
preco = (4.75, 5.75, 2.75, 1.20, 3.45, 5.70)
quantidade = (25,  30, 20, 80, 15, 12)
opc = str()


def escolhaProduto():
    produtoEscolhido = input('\nDigite o nome de um produto para saber o preço e a quantidade em estoque: ').capitalize()
    verificacaoEstoque(produtoEscolhido)
        
    
def verificacaoEstoque(produtoEscolhido):   
    print('-'*40)
    print(f'Nome\t\tQnt\t\tPreço') 
    if produtoEscolhido in produtos:
        produtos.index(produtoEscolhido)
        print(f'{produtoEscolhido:<17}{quantidade[produtos.index(produtoEscolhido)]:<16}{preco[produtos.index(produtoEscolhido)]}')
    else:
        print(f'Produto não encontrado no estoque.')
    print('-'*40)

while not opc == '0':
    opc = str()
    escolhaProduto()
    opc = input('\nDigite 0 para parar\nDeseja continuar? ')