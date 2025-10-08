from aluno import Aluno

class AlunoGraduacao(Aluno):
    nota_aprovacao = 7  # nota mínima para aprovação na graduação

    def __init__(self, nome, idade, curso, numero_matricula, semestre, nota1=0, nota2=0):
        super().__init__(nome, idade, curso, numero_matricula, nota1, nota2)
        self.__semestre = semestre

    # Getters e Setters
    def get_semestre(self):
        return self.__semestre
    
    def set_semestre(self, semestre):
        self.__semestre = semestre
