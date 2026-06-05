class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade
        
    def apresentar(self):
        print(f"Nome: {self.__nome}\nIdade: {self.__idade}")
    
    # Getter e setter de Nome    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        if novo_nome == "":
            print("Nome inválido, tente novamente.")
        self.__nome = novo_nome
    
    # Getter e setter de Idade
    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, nova_idade):
        if nova_idade < 0:
            print("Idade inválida, tente novamente.")
            return
        self.__idade = nova_idade