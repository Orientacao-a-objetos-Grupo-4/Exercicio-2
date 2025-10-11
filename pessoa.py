class Pessoa():
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    # Getters
    def get_nome(self):
        return self.__nome
    
    def get_idade(self):
        return self.__idade
    
    # Setters
    def set_nome(self, nome):
        self.__nome = nome

    def set_idade(self, idade):
        self.__idade = idade

    def __str__(self):
        return f"Nome: {self.__nome}, Idade: {self.__idade}"
