from time import sleep
from api.crud import User, Category, Product
import json
from views.interfaces import register_menu, remove_menu, list_menu, search_menu, product_search_menu, category_search_menu, update_menu
from datetime import datetime


def choose_operation_system(operation: int):
    match operation:
        case 1:
            choise_operation = register_menu()
            result = choose_operation_register(choise_operation)
            return result
        case 2:
            choise_operation = list_menu()
            result = choose_operation_list(choise_operation)
            return result
        case 3:
            choise_operation = search_menu()
            result = choose_operation_search(choise_operation)
            return result
        case 4:
            choise_operation = update_menu()
            result = choose_operation_update(choise_operation)
            return result
        case 5:
            choise_operation = remove_menu()
            result = choose_operation_remove(choise_operation)
            return result
        case 6:
            print('Obrigado, volte sempre!')
            return -1
        case 7:
            user = get_auth_user()
            print(f'Usuario {user["name"]} deslogado!')
            print('Obrigado, volte sempre!')
            logout()
            return -1
        case _:
            print('Opção invalida, sistema encerrado!')
            print('Obrigado, volte sempre!')
            return -1

def choose_operation_login(operation: int):
    match operation:
        case 1:
            print('Bem vindo ao login de usuario!')
            print('Precisaremos das seguintes informações!')
            sleep(2)
            print('E-mail')
            sleep(2)
            print('Senha')
            sleep(2)
            email = input('Informe seu email: ')
            password = input('Informe seu senha: ')
            
            result = login(email, password)
            return result
        case 2:
            print('Bem vindo ao cadastro de usuario!')
            print('Precisaremos das seguintes informações!')
            sleep(2)
            print('Nome completo')
            sleep(2)
            print('E-mail')
            sleep(2)
            print('Senha')
            sleep(2)
            name = input('Informe seu nome: ')
            email = input('Informe seu email: ')
            password = input('Informe seu senha: ')
            
            user = User(name, email, password)
            user.create()
            result = login(user.email, user.password)
            return result
            
        case 3:
            print('Obrigado, volte sempre!')
            logout()
            return -1
        case _:
            print('Opção invalida, sistema encerrado!')
            print('Obrigado, volte sempre!')
            logout()
            return -1

def login(email: str, password: str):
    with open('database/users.json', 'r') as json_file:
        users = list(json.loads(json_file.read()))
        for user in users:
            if user['email'] == email and user['password'] == password:
                with open('database/auth_user.json', 'w') as auth_user_file:
                    auth_user_file.write(json.dumps(user))
                print(f'{user["name"]} logado com sucesso!')
                return 1
        print('Usuario ou senha incorretos, tente novamente!')
        return 0
    
def logout():
    with open('database/auth_user.json', 'w') as auth_user_file:
        auth_user_file.write(json.dumps({}))

def verify_auth_user():
    with open('database/auth_user.json', 'r') as json_file:
        user = json.loads(json_file.read())
        return 1 if user != {} else -1

def get_auth_user():
    with open('database/auth_user.json', 'r') as json_file:
        user = json.loads(json_file.read())
        return user

def choose_operation_register(operation: int):
    match operation:
        case 1:
            print('Precisaremos das seguintes informações!')
            sleep(2)
            print('Nome do produto')
            sleep(2)
            print('Preço do produto')
            sleep(2)
            print('Quantos produtos tem no estoque')
            sleep(2)
            print('Validade do produto')
            sleep(2)
            print('ID da categoria')
            sleep(2)
            name = input('Informe o nome do produto: ')
            price = float(input('Informe o preço do produto: '))
            amount = int(input('Informe quantos produtos tem no estoque: '))
            has_validity = input('Este produto possui validade? S/N: ').upper()
            if has_validity == 'S':
                initial_validity = input('Informe a data de inicio da validade do produto( dia/mes/ano ): ')
                if date_validator(initial_validity) == False:
                    return 0
                final_validity = input('Informe a data de expiração da validade do produto( dia/mes/ano ): ')
                if date_validator(final_validity) == False:
                    return 0
                
                validity = initial_validity + ' - ' + final_validity
                
            elif has_validity == 'N':
                validity = 'Sem validade'
            else:
                print('Opção invalida, tente novamente!')
                return 0
            
            category = Category()
            categorys = category.get_all()
            if len(categorys) == 0:
                print('Sem categorias cadastradas!')
                return 0
            list(map(lambda category: print(f'{category["id"]} - {category["name"]}\n') ,categorys))
            id_category = int(input('Informe o ID da categoria: '))

            if category_validator(id_category) == False:
                return 0
            
            user = get_auth_user()
            id_user = user['id']
            product = Product(name, price, amount, validity, id_category, id_user)
            product.create()
            return 0
        case 2:
            print('Precisaremos das seguintes informações!')
            sleep(2)
            print('Nome da categoria')
            sleep(2)
            name = input('Informe o nome da categoria: ')
            user = get_auth_user()
            id_user = user['id']
            category = Category(name, id_user)
            category.create()
            return 0
        case 3:
            print('Cancelado!')
            return 0
        case _:
            print('Opção invalida!')
            return 0

def choose_operation_list(operation: int):
    match operation:
        case 1:
            print('Carregando produtos...')
            sleep(2)
            product = Product()
            products = product.get_all()
            
            if len(products) == 0:
                print('Sem produtos cadastrados')
                return 0
            print('='*50 + ' PRODUTOS ' + '='*50)
            for product in products:
                print(f"ID: {product['id']}\nNOME: {product['name']}\nPREÇO: {product['price']}\nQUANTIDADE: {product['amount']}\nVALIDADE: {product['validity']}\nID CATEGORIA: {product['id_category']}\nID USUARIO: {product['id_user']}")
                print('='*50 + '==========' + '='*50)
            return 0
        case 2:            
            print('Carregando categorias...')
            sleep(2)
            category = Category()
            categorys = category.get_all()
            
            if len(categorys) == 0:
                print('Sem categorias cadastradas')
                return 0
            
            print('='*50 + ' CATEGORIAS ' + '='*50)
            for category in categorys:
                print(f"ID: {category['id']}\nNOME: {category['name']}\nID USUARIO: {category['id_user']}")
                print('='*50 + '==========' + '='*50)
            return 0
        case 3:
            print('Cancelado!')
            return 0
        case _:
            print('Opção invalida!')
            return 0

def choose_operation_search(operation: int):
    match operation:
        case 1:
            choise_operation = product_search_menu()
            result = choose_operation_product_search(choise_operation)
            return result
        case 2:            
            choise_operation = category_search_menu()
            result = choose_operation_category_search(choise_operation)
            return result
        case 3:
            print('Cancelado!')
            return 0
        case _:
            print('Opção invalida!')
            return 0

def choose_operation_update(operation: int):
    match operation:
        case 1:
            print('Precisaremos das seguintes informações!')
            sleep(2)
            print('ID do produto')
            sleep(2)
            product = Product()
            products = product.get_all()
            if len(products) == 0:
                print('Sem produtos cadastrados!')
                return 0
            list(map(lambda product: print(f'{product["id"]} - {product["name"]}\n') ,products))
            id_product = int(input('Informe o ID do produto: '))
            if product_validator(id_product) == False:
                return 0
            
            print('Precisaremos das seguintes informações a serem atualizadas!')
            sleep(2)
            print('Nome do produto')
            sleep(2)
            print('Preço do produto')
            sleep(2)
            print('Quantos produtos tem no estoque')
            sleep(2)
            print('Validade do produto')
            sleep(2)
            print('ID da categoria')
            sleep(2)
            name = input('Informe o nome do produto: ')
            price = float(input('Informe o preço do produto: '))
            amount = int(input('Informe quantos produtos tem no estoque: '))
            has_validity = input('Este produto possui validade? S/N: ').upper()
            if has_validity == 'S':
                initial_validity = input('Informe a data de inicio da validade do produto( dia/mes/ano ): ')
                if date_validator(initial_validity) == False:
                    return 0
                final_validity = input('Informe a data de expiração da validade do produto( dia/mes/ano ): ')
                if date_validator(final_validity) == False:
                    return 0
                
                validity = initial_validity + ' - ' + final_validity
                
            elif has_validity == 'N':
                validity = 'Sem validade'
            else:
                print('Opção invalida, tente novamente!')
                return 0
            
            categorys = Category()
            list(map(lambda category: print(f'{category["id"]} - {category["name"]}\n') ,categorys.get_all()))
            id_category = int(input('Informe o ID da categoria: '))

            if category_validator(id_category) == False:
                return 0
            
            user = get_auth_user()
            id_user = user['id']
            product = Product(name, price, amount, validity, id_category, id_user, id_product)
            product.update()
            
            return 0
        case 2:
            print('Precisaremos das seguintes informações!')
            sleep(2)
            print('ID da categoria')
            sleep(2)
            category = Category()
            categorys = category.get_all()
            if len(categorys) == 0:
                print('Sem categorias cadastradas!')
                return 0
            list(map(lambda category: print(f'{category["id"]} - {category["name"]}\n') ,categorys))
            id_category = int(input('Informe o ID da categoria: '))
            if category_validator(id_category) == False:
                return 0
            
            print('Precisaremos das seguintes informações a serem atualizadas!')
            sleep(2)
            print('Nome do produto')
            sleep(2)
            
            name = input('Informe o nome da categoria: ')
            
            user = get_auth_user()
            id_user = user['id']
            category = Category(name, id_user, id_category)
            category.update()
            
            return 0
        case 3:
            print('Cancelado!')
            return 0
        case _:
            print('Opção invalida!')
            return 0

def choose_operation_remove(operation: int):
    match operation:
        case 1:
            print('Precisaremos das seguintes informações!')
            sleep(2)
            print('ID do produto')
            sleep(2)
            product = Product()
            products = product.get_all()
            if len(products) == 0:
                print('Sem produtos cadastrados!')
                return 0
            list(map(lambda product: print(f'{product["id"]} - {product["name"]}\n') ,products))
            id_product = int(input('Informe o ID do produto: '))
            if product_validator(id_product) == False:
                return 0
            product = Product(id=id_product)
            product.delete()
            return 0
        case 2:
            print('Atenção ao remover qualquer categoria, você irá remover todos os produtos relacionados!')
            print('')
            sleep(2)
            print('Precisaremos das seguintes informações!')
            sleep(2)
            print('ID da categoria')
            sleep(2)
            
            category = Category()
            categorys = category.get_all()
            if len(categorys) == 0:
                print('Sem categorias cadastradas!')
                return 0
            list(map(lambda category: print(f'{category["id"]} - {category["name"]}\n') ,categorys))
            id_category = int(input('Informe o ID da categoria: '))
            if category_validator(id_category) == False:
                return 0
            category = Category(id=id_category)
            category.delete()
            return 0
        case 3:
            print('Cancelado!')
            return 0
        case _:
            print('Opção invalida!')
            return 0

def date_validator(date: str):
    date_format = '%d/%m/%Y'
    try:
        datetime.strptime(date, date_format)
        return True
    except ValueError:
        print('Formato de data invalida, tente novamente!')
        return False

def category_validator(id_category: int):
    categorys = Category()
    ids_categorys = list(map(lambda category: category['id'],categorys.get_all()))
    if id_category not in ids_categorys:
        print('Categoria invalida, tente novamente!')
        return False
    else:
        return True

def product_validator(id_product: int):
    products = Product()
    ids_products = list(map(lambda product: product['id'],products.get_all()))
    if id_product not in ids_products:
        print('Produto invalido, tente novamente!')
        return False
    else:
        return True

def user_validator(id_user: int):
    users = User()
    ids_users = list(map(lambda user: user['id'],users.get_all()))
    if id_user not in ids_users:
        print('Usuario invalido, tente novamente!')
        return False
    else:
        return True

def choose_operation_product_search(operation: int):
    match operation:
        case 1:
            id = int(input('Informe um ID: '))
            field = 'id'
            value = id
        case 2:     
            name = input('Informe um nome: ')   
            field = 'name'
            value = name   
        case 3:
            price = input('Informe um preço: ')
            field = 'price'
            value = price
        case 4:
            amount = input('Informe uma quantidade: ')
            field = 'amount'
            value = amount
        case 5:
            has_validity = input('Este produto possui validade? S/N: ').upper()
            if has_validity == 'S':
                initial_validity = input('Informe a data de inicio da validade do produto( dia/mes/ano ): ')
                if date_validator(initial_validity) == False:
                    return 0
                final_validity = input('Informe a data de expiração da validade do produto( dia/mes/ano ): ')
                if date_validator(final_validity) == False:
                    return 0
                
                validity = initial_validity + ' - ' + final_validity
                
            elif has_validity == 'N':
                validity = 'Sem validade'
            else:
                print('Opção invalida, tente novamente!')
                return 0
            field = 'validity'
            value = validity
        case 6:
            category = Category()
            categorys = category.get_all()
            if len(categorys) == 0:
                print('Sem categorias cadastradas!')
                return 0
            list(map(lambda category: print(f'{category["id"]} - {category["name"]}\n') ,categorys))
            id_category = int(input('Informe o ID da categoria: '))
            if category_validator(id_category) == False:
                return 0
            field = 'id_category'
            value = id_category
        case 7:            
            user = User()
            users = user.get_all()
            if len(users) == 0:
                print('Sem usuarios cadastradas!')
                return 0
            list(map(lambda user: print(f'{user["id"]} - {user["name"]}\n') ,users))
            id_user = int(input('Informe o ID do usuario: '))
            if user_validator(id_user) == False:
                return 0
            field = 'id_user'
            value = id_user
        case _:
            print('Opção invalida!')
            return 0
        
    product = Product()
    products = product.search(field, value)
    print('Carregando produtos...')
    sleep(2)
    
    if len(products) == 0:
        print('Sem produtos cadastrados')
        return 0
    
    print('='*50 + ' PRODUTOS ' + '='*50)
    for product in products:
        print(f"ID: {product['id']}\nNOME: {product['name']}\nPREÇO: {product['price']}\nQUANTIDADE: {product['amount']}\nVALIDADE: {product['validity']}\nID CATEGORIA: {product['id_category']}\nID USUARIO: {product['id_user']}")
        print('='*50 + '==========' + '='*50)
    return 0

def choose_operation_category_search(operation: int):
    match operation:
        case 1:
            id = int(input('Informe um ID: '))
            field = 'id'
            value = id
        case 2:     
            name = input('Informe um nome: ')   
            field = 'name'
            value = name   
        case 3:            
            user = User()
            users = user.get_all()
            if len(users) == 0:
                print('Sem usuarios cadastradas!')
                return 0
            list(map(lambda user: print(f'{user["id"]} - {user["name"]}\n') ,users))
            id_user = int(input('Informe o ID do usuario: '))
            if user_validator(id_user) == False:
                return 0
            field = 'id_user'
            value = id_user
        case _:
            print('Opção invalida!')
            return 0
        
    category = Category()
    categorys = category.search(field, value)
    print('Carregando categorias...')
    sleep(2)
    
    if len(categorys) == 0:
        print('Sem categorias cadastradas')
        return 0
    
    print('='*50 + ' CATEGORIAS ' + '='*50)
    for category in categorys:
        print(f"ID: {category['id']}\nNOME: {category['name']}\nID USUARIO: {category['id_user']}")
        print('='*50 + '==========' + '='*50)
    return 0