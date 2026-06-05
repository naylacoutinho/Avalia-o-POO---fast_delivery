from modelos.entrega import EntregaComum, EntregaExpressa, EntregaPremium

class EntregaService:
    def criar_entrega(self, tipo, distancia):
        if tipo == "1":
            return EntregaComum(distancia)
        elif tipo == "2":
            return EntregaExpressa(distancia)
        elif tipo == "3":
            return EntregaPremium(distancia)
        else:
            raise ValueError("Tipo de entrega inválido.")