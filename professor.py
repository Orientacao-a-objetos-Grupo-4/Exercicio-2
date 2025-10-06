from pessoa import Pessoa

class Profressor(Pessoa):
    def __init__(self, nome, idade, disciplina):
        super().__init__(nome, idade)
        self.disciplina = disciplina
        self.alunos = []