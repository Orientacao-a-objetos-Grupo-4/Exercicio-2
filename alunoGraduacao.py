from aluno import Aluno

class AlunoGraduacao(Aluno):
    nota_aprovacao = 7
    
    def __init__(self, nome, idade, curso, semestre):
        super().__init__(nome, idade, curso)
        self.__semestre = semestre
    
    def get_semestre(self):
        return self.__semestre
    
    def set_semestre(self, semestre):
        self.__semestre = semestre
