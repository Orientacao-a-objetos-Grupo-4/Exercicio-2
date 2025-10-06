
import abc
from pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)
        self.numero_matricula = 0
        self.nota1 = 0
        self.nota2 = 0

    def getMatricula(self):
        return self.numero_matricula
    
    def setMatricula(self, matricula):
        self.numero_matricula = matricula

    def setNota1(self, nota1):
        self.nota1 = nota1

    def setNota2(self, nota2):
        self.nota2 = nota2

    def getNota1(self):
        return self.nota1
    
    def getNota2(self):
        return self.nota2

    def calcular_media(self):
        media = (self.nota1 + self.nota2) / 2
        return media
    
    
    @abc.abstractmethod
    def verificar_aprovado(self):
        pass

    @abc.abstractmethod
    def printarSituacao(self,aprovado):
        pass