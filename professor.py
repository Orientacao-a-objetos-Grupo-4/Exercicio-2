from pessoa import Pessoa

class Profressor(Pessoa):
    def __init__(self, nome, idade, titulacaoMaxima):
        super().__init__(nome, idade)
        self.titulacaoMaxima = titulacaoMaxima