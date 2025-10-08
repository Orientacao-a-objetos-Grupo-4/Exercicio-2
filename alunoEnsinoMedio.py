from aluno import Aluno

class AlunoEnsinoMedio(Aluno):
    nota_aprovacao = 6

    def __init__(self, nome, idade, curso, serie,nota1,nota2,notaAprovacao):
        super().__init__(nome, idade, curso)
        self.__serie = serie

    def getSerie(self):
        return self.__serie
    
    def setSerie(self, serie):
        self.__serie = serie


    