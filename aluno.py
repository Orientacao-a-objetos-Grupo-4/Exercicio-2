
from pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)
        self.numero_matricula = 0
        self.__nota1 = 0
        self.__nota2 = 0


    def setMatricula(self, matricula):
        self.numero_matricula = matricula

    def getMatricula(self):
        return self.numero_matricula

    def setNota1(self, nota1):
        self.__nota1 = nota1

    def setNota2(self, nota2):
        self.__nota2 = nota2
    
    def getNota1(self):
        return self.__nota1
    
    def getNota2(self):
        return self.__nota2