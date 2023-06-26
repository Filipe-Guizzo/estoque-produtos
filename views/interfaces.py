
def main_menu():
    print('Olá seja bem vindo ao sistema de estoque de produtos!')
    print('Escolha uma das seguites opções para prosseguir:')
    operation  = int(input('1 - Cadastro\n2 - Listar\n3 - Pesquisar\n4 - Atualizar\n5 - Remover\n\033[31m6 - Encerrar sistema\n7 - Sair\n\033[0mO que deseja fazer?: '))
    return operation

def login_menu():
    print('Olá seja bem vindo, este é o login do sistema!')
    operation = int(input('1 - Fazer login\n2 - Fazer cadastro\n\033[31m3 - Sair\n\033[0mO que deseja fazer?: '))
    return operation

def register_menu():
    print('Escolha o que você deseja cadastrar: ')
    operation = int(input('1 - Produto\n2 - Categoria\n\033[31m3 - Cancelar\n\033[0mO que deseja fazer?: '))
    return operation

def list_menu():
    print('Escolha o que você deseja listar: ')
    operation = int(input('1 - Produto\n2 - Categoria\n\033[31m3 - Cancelar\n\033[0mO que deseja fazer?: '))
    return operation

def search_menu():
    print('Escolha o que você deseja pesquisar: ')
    operation = int(input('1 - Produto\n2 - Categoria\n\033[31m3 - Cancelar\n\033[0mO que deseja fazer?: '))
    return operation

def update_menu():
    print('Escolha o que você deseja atualizar: ')
    operation = int(input('1 - Produto\n2 - Categoria\n\033[31m3 - Cancelar\n\033[0mO que deseja fazer?: '))
    return operation

def remove_menu():
    print('Escolha o que você deseja remover: ')
    operation = int(input('1 - Produto\n2 - Categoria\n\033[31m3 - Cancelar\n\033[0mO que deseja fazer?: '))
    return operation

def product_search_menu():
    print('Qual campo de produto você deseja realizar a pesquisa: ')
    operation = int(input('1 - ID\n2 - Nome\n3 - Preço\n4 - Quantidade\n5 - Validade\n6 - Categoria\n7 - Usuario\nO que deseja fazer?: '))
    return operation

def category_search_menu():
    print('Qual campo de categoria você deseja realizar a pesquisa: ')
    operation = int(input('1 - ID\n2 - Nome\n3 - Usuario\nO que deseja fazer?: '))
    return operation