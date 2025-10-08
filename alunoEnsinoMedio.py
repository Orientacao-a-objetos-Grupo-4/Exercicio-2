from aluno import Aluno

class AlunoEnsinoMedio(Aluno):
    def __init__(self, nome, idade, curso, serie):
        super().__init__(nome, idade, curso)
        self.serie = serie

    def setSerie(self, serie):
        self.serie = serie

    def getSerie(self):
        return self.serie
    

    