"""Nossa ideia seria um cadastro de produtos em geral sendo como um estoque podendo cadastrar os produtos, pesquisar por um determinado produto já cadastrado abrangendo mais funções que serão colocadas quando estiver sendo desenvolvido tendo um diferencial que seria usado junto com um banco de dados."""
from views.interfaces import main_menu, login_menu
from functions.operations import choose_operation_system, choose_operation_login, verify_auth_user

while True:
    if verify_auth_user() == -1:
        operation = login_menu()
        result = choose_operation_login(operation)
        if result == 0:
            continue
        if result == -1:
            break
    operation = main_menu()
    result = choose_operation_system(operation)
    if result == 0:
        continue
    if result == -1:
        break
