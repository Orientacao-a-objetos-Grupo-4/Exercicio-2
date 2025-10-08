from pessoa import Pessoa

class Profressor(Pessoa):
    def __init__(self, nome, idade, titulacaoMaxima):
        super().__init__(nome, idade)
        self.__titulacaoMaxima = titulacaoMaxima

    def getTitulacaoMaxima(self):
        return self.titulacaoMaxima
    
    def setTitulacaoMaxima(self, titulacaoMaxima):
        self.titulacaoMaxima = titulacaoMaxima