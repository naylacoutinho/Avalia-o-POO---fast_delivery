from modelos.pedido import Pedido

class PedidoService:
    def __init__(self):
        self.pedidos = []

    def criar_pedido(self, codigo, cliente, peso, distancia, tipo_entrega, frete):
        pedido = Pedido(codigo, cliente, peso, distancia, tipo_entrega, frete)
        self.pedidos.append(pedido)
        return pedido

    def listar(self):
        return self.pedidos

    def buscar(self, codigo):
        for pedido in self.pedidos:
            if pedido.codigo == codigo:
                pedido.informacoes()
        return
    
    def atualizar_status(self, codigo, novo_status):
        for pedido in self.pedidos:
            if pedido.codigo == codigo:
                pedido.atualizar_status(novo_status)
                return pedido
        return