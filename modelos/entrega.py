from interfaces.calculo_frete_interface import CalculoFreteInterface

class Entrega(CalculoFreteInterface):
    def __init__(self, distancia):
        self.__distancia = distancia
    
    @property
    def distancia(self):
        return self.__distancia

class EntregaComum(Entrega):
    def __init__(self, distancia):
        super().__init__(distancia)
        
    def calcular_frete(self):
        return self.distancia * 1.5

class EntregaExpressa(Entrega):
    def __init__(self, distancia):
        super().__init__(distancia)
        
    def calcular_frete(self):
        return self.distancia * 3

class EntregaPremium(Entrega):
    def __init__(self, distancia):
        super().__init__(distancia)
        
    def calcular_frete(self):
        return self.distancia * 5 + 20