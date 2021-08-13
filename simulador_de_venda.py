"""
Exercício geral de Python

Objetivo: criar um sistema de simualão de venda de produtos.

OBS.: O objetivo do programa é simular a venda de produtos exibidos ao usuário.
OBS.2: É possível cadastrar novos produtos nas funções e aumentar o valor do range em 'num_produtos'.

"""


def consulta_preco(produto):
    """Consulta o preço do produto de acordo com o seu número."""
    if produto == 1:
        return 20.00
    elif produto == 2:
        return 30.00
    elif produto == 3:
        return 3000.00
    elif produto == 4:
        return 35.00
    elif produto == 5:
        return 250.00
    elif produto == 6:
        return 500.00
    elif produto == 7:
        return 150.00
    else:
        return 00


def nome_produto(produto):
    """Consulta o nome do produto de acordo com o seu número."""
    if produto == 1:
        return 'Fone de ouvido'
    elif produto == 2:
        return 'Carregador de celular'
    elif produto == 3:
        return 'Notebook'
    elif produto == 4:
        return 'Mouse'
    elif produto == 5:
        return 'TV Box'
    elif produto == 6:
        return 'Câmera fotográfica'
    elif produto == 7:
        return 'Smartwatch'
    else:
        return 'Produto inválido.'


###########################################

num_produtos = list(range(1, 8))
subtotal = {}

nomes = list(map(nome_produto, num_produtos))
precos = list(map(consulta_preco, num_produtos))
produtos_dict = {nomes[i]: precos[i] for i in range(0, len(nomes))}

produtos_list = []

key = 1
indice = 0
total = {}

############################################


def venda_principal():
    """Função do fluxo principal do programa"""
    global total
    print("\n" * 130)
    contador = 1
    print('Escolha o número do produto: ')

    for nome, valor in produtos_dict.items():
        print(contador, '-', nome, '-', f'R${valor}')
        contador += 1

    produtos_list.append(int(input('>>> ')))

    print("\n" * 130)

    # Exibindo ao cliente os produtos no carrinho
    print('Produtos no carrinho:')
    for prod in produtos_list:
        print(f'>>Produto: {nome_produto(prod)} \n>>Preço: R${consulta_preco(prod)} \n-------')
        subtotal[nome_produto(prod)] = consulta_preco(prod)
        total = subtotal.copy()

    # Decisão para encerrar o fluxo de compra, continuar ou remover algum item:
    controle = int(input('Digite 1 para continuar comprando, 2 para encerrar a compra ou 3 para remover '
                         'um ítem do carrinho: \n>>> '))

    if controle == 1:
        venda_principal()

    elif controle == 2:
        encerrar_venda()

    elif controle == 3:
        remover_item()
    else:
        print('Operação inválida.')


############################################


def encerrar_venda():
    """Função para encerrar a venda dos produtos"""
    print('-------')

    # Informa o total dos produtos no carrinho:
    print(f'Total: R${sum(total.values())}')

    # Verifica se o cliente deseja finalizar o pagamento:
    controle_2 = int(input('Digite 1 para finalizar o pagamento ou 2 para cancelar a compra: \n>>> '))

    if controle_2 == 1:
        print("\n" * 130)
        email = input('Digite o seu email: ')
        endereco = input('Digite o CEP e número da sua residência: ')
        print(f'As informações de envio e o boleto foram enviados para o email "{email}". '
              f'\nObrigado por comprar conosco!')

    elif controle_2 == 2:
        print("\n" * 130)
        print('Volte sempre!')

    else:
        print('Operação inválda.')
        encerrar_venda()


##############################################


def remover_item():
    """Função para remover itens do carrinho"""
    contador = 1
    print("\n" * 130)
    print('Digite o número do produto: ')

    for nome in produtos_dict.keys():
        print(contador, '-', nome)
        contador += 1

    item = int(input('>>> '))

    ind = produtos_list.index(item)

    for name, preco in subtotal.items():
        if nome_produto(item) == name and consulta_preco(item) == preco:
            total.pop(nome_produto(item))
            produtos_list.pop(ind)

        print("\n" * 130)
        print('Produto removido com sucesso!')
        print('-------')

    # Decisão para encerrar o fluxo de compra, continuar ou remover algum item:
    controle = int(input('Digite 1 para continuar comprando, 2 para encerrar a compra ou 3 para remover '
                         'um ítem do carrinho: \n>>> '))

    if controle == 1:
        venda_principal()

    elif controle == 2:
        encerrar_venda()

    elif controle == 3:
        remover_item()
    else:
        print('Operação inválida.')


# Inicio

venda_principal()
