from modelos.cliente import Cliente

class ClienteService():
    def __init__(self):
        self.clientes = []
        
    def cadastrar(self, nome, idade, cpf, contato, endereco):
        cliente = Cliente(nome, idade, cpf, contato, endereco)
        self.clientes.append(cliente)
        return cliente
    
    def listar(self):
        return self.clientes
    
    def buscar(self, cpf):
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                return cliente
        return