from aluno import Aluno

class AlunoEnsinoMedio(Aluno):
    def __init__(self, nome, idade, curso, semestre):
        super().__init__(nome, idade, curso)
        self.semestre = semestre