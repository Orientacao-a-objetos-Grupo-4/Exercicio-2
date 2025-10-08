from pessoa import Pessoa

class Profressor(Pessoa):
    def __init__(self, nome, idade, titulacaoMaxima):
        super().__init__(nome, idade)
        self.__titulacaoMaxima = titulacaoMaxima

    def getTitulacaoMaxima(self):
        return self.__titulacaoMaxima
    
    def setTitulacaoMaxima(self, titulacaoMaxima):
        self.__titulacaoMaxima = titulacaoMaxima

    def __str__(self):
        return f"Nome do Professor: {self.get_nome()}, Idade: {self.get_idade()}, Titulação: {self.getTitulacaoMaxima()}"