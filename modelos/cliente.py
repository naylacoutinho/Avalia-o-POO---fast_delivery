from modelos.pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome, idade, cpf, contato, endereco):
        super().__init__(nome, idade)
        self.__cpf = cpf
        self.__contato = contato
        self.__endereco = endereco
    
    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def contato(self):
        return self.__contato
    
    @property
    def endereco(self):
        return self.__endereco
    
    def comprar(self, produto):
        print(f'{self.nome} está comprando {produto}')
        
    def apresentar(self):
        print(f"Nome: {self.nome}\nIdade: {self.idade}\nCpf: {self.cpf}\nContato: {self.contato}\nEnderço: {self.endereco}")
        