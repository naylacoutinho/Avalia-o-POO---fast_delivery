class Pedido:
    STATUS = ["Em preparação", "Saiu para entrega", "Entregue", "Cancelado"]

    def __init__(self, codigo, cliente, peso, distancia, tipo_entrega, frete):
        self.__codigo = codigo
        self.__cliente = cliente
        self.__peso = peso
        self.__distancia = distancia
        self.__tipo_entrega = tipo_entrega
        self.__frete = frete
        self.__status = Pedido.STATUS[0]

    @property
    def codigo(self):
        return self.__codigo

    @property
    def cliente(self):
        return self.__cliente

    @property
    def peso(self):
        return self.__peso

    @property
    def distancia(self):
        return self.__distancia

    @property
    def frete(self):
        return self.__frete

    @property
    def status(self):
        return self.__status

    def atualizar_status(self, novo_status):
        if novo_status not in Pedido.STATUS:
            raise ValueError("Status inválido.")
        self.__status = novo_status

    def informacoes(self):
        print(f"Pedido {self.codigo}\nCliente: {self.cliente.nome}\nPeso: {self.peso}\nDistância: {self.distancia}\nStatus: {self.status}\nFrete: R${self.frete:.2f}")