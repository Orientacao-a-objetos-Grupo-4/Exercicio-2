
import abc
from pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)
        self.numero_matricula = 0
        self.__nota1 = 0
        self.__nota2 = 0
