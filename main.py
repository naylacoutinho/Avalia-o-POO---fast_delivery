from services.cliente_service import ClienteService
from services.pedido_service import PedidoService
from services.entrega_service import EntregaService
from services.entregador_service import EntregadorService
from util.menu import menu_principal, menu_clientes, menu_pedidos, menu_entregadores
from util.formatador import linha

cliente_service = ClienteService() # Criando uma lista de Clientes
pedido_service = PedidoService() # Criando uma lista de Pedidos
entrega_service = EntregaService() # Criando um objeto entrega, dos tipos comum, expressa e premium
entregador_service = EntregadorService() # Criando uma lista de Entregadores

while True:
    opcao = menu_principal() # Imprimir o menu e receber a opção escolhida

    if opcao == "1": # Clientes
        op = menu_clientes() # Imprimir o menu de clientes e receber a opção escolhida

        if op == "1": # Cadastrar um novo cliente
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            cpf = input("CPF: ")
            teste = cliente_service.buscar(cpf) # procura pelo cpf
            if not teste: # Verifica se o cliente existe
                tel = input("Telefone: ")
                end = input("Endereço: ")
                cliente_service.cadastrar(nome, idade, cpf, tel, end) 
                print(f"Cliente {nome} cadastrado!")
            else:
                print("Cpf já cadastrado, tente novamente.")

        elif op == "2": # Listar os clientes
            lista_clientes = cliente_service.listar() # Adiciona um novo objeto à lista
            for c in lista_clientes:
                linha()
                c.apresentar() # Exibe as informações de cada objeto

        elif op == "3": # Buscar os clientes
            cpf = input("CPF do cliente: ")
            cli = cliente_service.buscar(cpf) # Busca clientes pelo cpf
            if cli:
                cli.apresentar()
            else:
                print("Cliente não encontrado.")
            
        else:
            print("Opção inválida, tente novamente...")

    elif opcao == "2": # Pedidos
        op = menu_pedidos() # Imprimir o menu de pedidos e receber a opção escolhida

        if op == "1":
            codigo = input("Código: ")
            cliente_cpf = input("CPF do cliente: ")
            cliente = cliente_service.buscar(cliente_cpf) # procura pelo cpf
            if not cliente: # Verifica se o cliente existe
                print("Cliente não encontrado.")
                
            else:
                peso = float(input("Peso (kg): "))
                distancia = float(input("Distância (km): ")) 

                tipo = input("Tipo de entrega (digite apenas o número: 1 comum/ 2 expressa/ 3 premium): ")
                entrega = entrega_service.criar_entrega(tipo, distancia) # Criando a entrega
                frete = entrega.calcular_frete() # Calculanado frete

                pedido_service.criar_pedido(codigo, cliente, peso, distancia, tipo, frete) # Criando o pedido
                print(f"Pedido criado! Frete: R$ {frete:.2f}")

        elif op == "2": # Listar pedidos
            for p in pedido_service.listar():
                linha()
                p.informacoes()

        elif op == "3": # Atualizar status pedido
            codigo = input("Código do pedido: ")
            print("Status disponíveis:")
            for s in ["Em preparação", "Saiu para entrega", "Entregue", "Cancelado"]:
                print("-", s)
            novo = input("Novo status: ")

            ped = pedido_service.atualizar_status(codigo, novo)
            if ped:
                print("Atualizado!")
            else:
                print("Pedido não encontrado.")
        else:
            print("Opção inválida, tente novamente...")
            
    elif opcao == "3":

        op = menu_entregadores()

        if op == "1":
            nome = input("Nome: ")
            veiculo = input("Veículo: ")
            cnh = input("CNH: ")

            teste = entregador_service.buscar(cnh)

            if not teste:
                entregador_service.cadastrar(nome, veiculo, cnh)
                print("Entregador cadastrado!")
            else:
                print("CNH já cadastrada.")

        elif op == "2":
            lista_entregadores = entregador_service.listar()

            for e in lista_entregadores:
                linha()
                e.apresentar()

        elif op == "3":
            cnh = input("CNH do entregador: ")

            entregador = entregador_service.buscar(cnh)

            if entregador:
                entregador.apresentar()
            else:
                print("Entregador não encontrado.")

    elif opcao == "0":
        print("Encerrando, obrigada por usar o sistema!")
        break
    
    else:
        print("Opção inválida, tente novamente...")