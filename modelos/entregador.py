from modelos.pessoa import Pessoa

class Entregador(Pessoa):
    def __init__(self, nome, idade, veiculo, cnh):
        super().__init__(nome, idade)
        self.__veiculo = veiculo
        self.__cnh = cnh

    @property
    def veiculo(self):
        return self.__veiculo

    @property
    def cnh(self):
        return self.__cnh

    def entregar(self):
        print(f"{self.nome} está entregando o pedido.")
        
    def apresentar(self):
        print(f"Nome: {self.nome}\nVeículo: {self.veiculo}\nCNH: {self.cnh}")