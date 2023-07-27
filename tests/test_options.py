import sys
from Contato import Contato

def test_helper() -> None:
    print("Como usar o tests.py: python tests.py <método> <*argumentos>")
    print("Argumentos disponíveis:") 
    print("""\n- create <nome> <sobrenome> <email> <telefone>
                \n- read <id>
                \n*- update <id> <nome> e/ou <sobrenome> e/ou <email> e/ou <telefone>
                \n- delete <id>
                \n- search <nome>""")
    sys.exit(1)
    
def option_create(dados) -> None:
    if len(sys.argv) == 6:
        dados['Nome'] = sys.argv[2]
        dados['Sobrenome'] = sys.argv[3]
        dados['Email'] = sys.argv[4]
        dados['Telefone'] = sys.argv[5]
        response = Contato().create_contato(dados)
        if response:
            Contato().read_contato(response["ID"])
    else:
        print("É necessário adicionar todos os dados em ordem:")
        print(">_ create <Nome> <Sobrenome> <Email> <Telefone>\n")
    sys.exit(1)
    
def option_read() -> None:
    if len(sys.argv) == 3:
        Contato().read_contato(sys.argv[2])
    sys.exit(1)

def option_update(dados) -> None:
    if len(sys.argv) == 6:
        if not "." in sys.argv[3]:
            dados['Nome'] = sys.argv[3]
        if not "." in sys.argv[4]:
            dados['Email'] = sys.argv[4]
        if not "." in sys.argv[5]:
            dados['Telefone'] = sys.argv[5]
        if sys.argv[3] == "." and sys.argv[4] == "." and sys.argv[5] == ".":
            print("É necessário adicionar pelo menos 1 dado pra atualizar")
        else:
            response = Contato().update_contato(sys.argv[2], dados)
            if response:
                Contato().read_contato(sys.argv[2])
    else:
        print("É necessário adicionar os dados:")
        print(">_ update <Nome> e/ou <Email> e/ou <Telefone>\n")
        print("Por exemplo, caso você queira somente atualizar Sobrenome e Telefone:")
        print(""">_ update . . <Telefone>""")
    sys.exit(1)

def option_delete() -> None:
    if len(sys.argv) == 3:
        response = Contato().delete_contato(sys.argv[2])
        if response:
            Contato().read_contato(sys.argv[2])
    sys.exit(1)

def option_search() -> None:
    if len(sys.argv) == 3:
        response = Contato().search_contato(sys.argv[2])
        if response:
            for contato in response:
                print(contato)
    sys.exit(1)
    
def options(dados) -> None:
    if sys.argv[1] == "create":
        option_create(dados)
    elif sys.argv[1] == "read":
        option_read()
    elif sys.argv[1] == "update":
        option_update(dados)
    elif sys.argv[1] == "delete":
        option_delete()
    elif sys.argv[1] == "search":
        option_search()
    else:
        test_helper()

def run_tests() -> None:
    dados = {}
    if len(sys.argv) > 1:
        options(dados)
    else:
        test_helper()