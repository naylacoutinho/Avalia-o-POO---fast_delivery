from modelos.entregador import Entregador

class EntregadorService:
    def __init__(self):
        self.entregadores = []

    def cadastrar(self, nome, veiculo, cnh):
        entregador = Entregador(nome, veiculo, cnh)
        self.entregadores.append(entregador)
        return entregador

    def listar(self):
        return self.entregadores

    def buscar(self, cnh):
        for entregador in self.entregadores:
            if entregador.cnh == cnh:
                return entregador
        return