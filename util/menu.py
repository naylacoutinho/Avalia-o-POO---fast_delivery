from util.validador import validar_opcao
from util.formatador import linha

def menu_principal():
    linha()
    print("\tFAST DELIVERY EXPRESS")
    print("1 - Clientes")
    print("2 - Pedidos")
    print("3 - Entregadores")
    print("0 - Sair")
    return validar_opcao(["1", "2", "3", "0"])

def menu_clientes():
    linha()
    print("\tMENU CLIENTES")
    print("1 - Cadastrar cliente")
    print("2 - Listar clientes")
    print("3 - Buscar cliente")
    print("0 - Voltar")
    return validar_opcao(["1", "2", "3", "0"])

def menu_pedidos():
    linha()
    print("\tMENU PEDIDOS")
    print("1 - Criar pedido")
    print("2 - Listar pedidos")
    print("3 - Atualizar status")
    print("0 - Voltar")
    return validar_opcao(["1", "2", "3", "0"])

def menu_entregadores():
    linha()
    print("\tMENU ENTREGADORES")
    print("1 - Cadastrar entregador")
    print("2 - Listar entregadores")
    print("3 - Buscar entregador")
    print("0 - Voltar")
    return validar_opcao(["1", "2", "3", "0"])