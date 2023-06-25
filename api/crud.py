import json

class Product:
    def __init__(self,name: str='', price: float=0.0, amount:int=0, validity: str='', id_category: int=0, id_user: int=0, id: int=0):
        self.id = id
        self.name = name
        self.price = price
        self.amount = amount
        self.validity = validity
        self.id_category = id_category
        self.id_user = id_user
    
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value: int):
        self._id = value
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value: str):
        self._name = value
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value: float):
        self._price = value
    
    @property
    def amount(self):
        return self._amount
    
    @amount.setter
    def amount(self, value: int):
        self._amount = value
    
    @property
    def validity(self):
        return self._validity
    
    @validity.setter
    def validity(self, value: str):
        self._validity = value
    
    @property
    def id_category(self):
        return self._id_category
    
    @id_category.setter
    def id_category(self, value: int):
        self._id_category = value
    
    @property
    def id_user(self):
        return self._id_user
    
    @id_user.setter
    def id_user(self, value: int):
        self._id_user = value
    
    def __str__(self):
        return self.name

    def create(self):
        try:
            with open('database/products.json', 'r') as json_file:
                products = list(json.loads(json_file.read()))
                size = len(products)
                id = products[size-1]['id'] + 1
        except (json.decoder.JSONDecodeError,IndexError):
            print('AVISO: arquivo em branco ou com dados invalidos, resetando arquivo!')
            products = list()
            id = 1

        self.id = id
        product = dict()
        product['id'] = self.id
        product['name'] = self.name
        product['price'] = self.price
        product['amount'] = self.amount
        product['price'] = self.price
        product['validity'] = self.validity
        product['id_category'] = self.id_category
        product['id_user'] = self.id_user
        products.append(product)
        with open('database/products.json', 'w') as json_file:
            json_file.write(json.dumps(products))
        print('Produto criado com sucesso!')
    
    def get_all(self):
        with open('database/products.json', 'r') as json_file:
            products = json.loads(json_file.read())
            return list(products)
    
    def search(self, field: str, value):
        products = self.get_all()
        filter_products = list()
        if field == 'name':        
            for product in products:
                if str(value).lower() in str(product['name']).lower():
                    filter_products.append(product)
        else:
            for product in products:
                if value == product[f'{field}']:
                    filter_products.append(product)
        return filter_products
    
    def update(self):
        products = self.get_all()

        for product in products:
            if product['id'] == self.id:
                product['name'] = self.name
                product['price'] = self.price
                product['amount'] = self.amount
                product['price'] = self.price
                product['validity'] = self.validity
                product['id_category'] = self.id_category
                product['id_user'] = self.id_user
        with open('database/products.json', 'w') as json_file:
            json_file.write(json.dumps(products))
        print('Produto atualizado com sucesso!')
    
    def delete(self):
        id_product = self.id
        products = self.get_all()
        for product in products:
            if product['id'] == id_product:
                products.pop(products.index(product))
        with open('database/products.json', 'w') as json_file:
            json_file.write(json.dumps(products))
        print('Produto removido com sucesso!')

class Category:
    product = Product()
    
    def __init__(self, name: str='', id_user: int='', id: int=0):
        self.id = id
        self.name = name
        self.id_user = id_user
    
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value: int):
        self._id = value
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value: str):
        self._name = value
    
    @property
    def id_user(self):
        return self._id_user
    
    @id_user.setter
    def id_user(self, value: int):
        self._id_user = value
    
    def __str__(self):
        return self.name
    
    def create(self):
        try:
            with open('database/categorys.json', 'r') as json_file:
                categorys = list(json.loads(json_file.read()))
                size = len(categorys)
                id = categorys[size-1]['id'] + 1
        except (json.decoder.JSONDecodeError,IndexError):
            print('AVISO: arquivo em branco ou com dados invalidos, resetando arquivo!')
            categorys = list()
            id = 1

        self.id = id
        category = dict()
        category['id'] = self.id
        category['name'] = self.name
        category['id_user'] = self.id_user
        categorys.append(category)
        with open('database/categorys.json', 'w') as json_file:
            json_file.write(json.dumps(categorys))
        print('Categoria criada com sucesso!')
    
    def get_all(self):
        with open('database/categorys.json', 'r') as json_file:
            categorys = json.loads(json_file.read())
            return list(categorys)
    
    def search(self, field: str, value):
        categorys = self.get_all()
        filter_categorys = list()
        if field == 'name':        
            for category in categorys:
                if str(value).lower() in str(category['name']).lower():
                    filter_categorys.append(category)
        else:
            for category in categorys:
                if value == category[f'{field}']:
                    filter_categorys.append(category)
        return filter_categorys
    
    def update(self):
        categorys = self.get_all()

        for category in categorys:
            if category['id'] == self.id:
                category['name'] = self.name
                category['id_user'] = self.id_user
        with open('database/categorys.json', 'w') as json_file:
            json_file.write(json.dumps(categorys))
        print('Categoria atualizada com sucesso!')
    
    def delete(self):
        id_category = self.id
        categorys = self.get_all()
        products = self.product.get_all()
        
        #remove products
        for product in products:
            if product['id_category'] == id_category:
                products.pop(products.index(product))
        with open('database/products.json', 'w') as json_file:
            json_file.write(json.dumps(products))
        
        #remove categorys
        for category in categorys:
            if category['id'] == id_category:
                categorys.pop(categorys.index(category))
        with open('database/categorys.json', 'w') as json_file:
            json_file.write(json.dumps(categorys))
            
        print('Categoria removida com sucesso!')
        
class User:
    product = Product()
    category = Category()
    
    def __init__(self, name: str='', email: str='', password: str='', id: int=0):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
    
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value: int):
        self._id = value
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value: str):
        self._name = value
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value: str):
        self._email = value
    
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, value: str):
        self._password = value
    
    def __str__(self):
        return self.name
    
    def create(self):
        try:
            with open('database/users.json', 'r') as json_file:
                users = list(json.loads(json_file.read()))
                size = len(users)
                id = users[size-1]['id'] + 1
        except (json.decoder.JSONDecodeError,IndexError):
            print('AVISO: arquivo em branco ou com dados invalidos, resetando arquivo!')
            users = list()
            id = 1

        self.id = id
        user = dict()
        user['id'] = self.id
        user['name'] = self.name
        user['email'] = self.email
        user['password'] = self.password
        users.append(user)
        with open('database/users.json', 'w') as json_file:
            json_file.write(json.dumps(users))
        print('Usuario criado com sucesso!')
        
    def get_all(self):
        with open('database/users.json', 'r') as json_file:
            users = json.loads(json_file.read())
            return list(users)
    
    def search(self, field: str, value):
        users = self.get_all()
        filter_users = list()
        if field == 'name':        
            for user in users:
                if str(value).lower() in str(user['name']).lower():
                    filter_users.append(user)
        else:
            for user in users:
                if value == user[f'{field}']:
                    filter_users.append(user)
        return filter_users
    
    def update(self):
        users = self.get_all()

        for user in users:
            if user['id'] == self.id:
                user['name'] = self.name
                user['email'] = self.email
                user['password'] = self.password
        with open('database/users.json', 'w') as json_file:
            json_file.write(json.dumps(users))
        print('Usuario atualizado com sucesso!')
    
    def delete(self):
        id_user = self.id
        users = self.get_all()
        categorys = self.category.get_all()
        products = self.product.get_all()
        ids_categorys = list()
        
        #remove categorys
        for category in categorys:
            if category['id_user'] == id_user:
                categorys.pop(categorys.index(category))
                ids_categorys.append(category['id'])
        with open('database/categorys.json', 'w') as json_file:
            json_file.write(json.dumps(categorys))
        
        #remove products
        for product in products:
            if product['id_category'] in ids_categorys:
                products.pop(products.index(product))
            if product['id_user'] == id_user:
                products.pop(products.index(product))
        with open('database/products.json', 'w') as json_file:
            json_file.write(json.dumps(products))
        
        #remove users
        for user in users:
            if user['id'] == id_user:
                users.pop(users.index(user))
        with open('database/users.json', 'w') as json_file:
            json_file.write(json.dumps(users))
            
        print('Usuario removido com sucesso!')
    