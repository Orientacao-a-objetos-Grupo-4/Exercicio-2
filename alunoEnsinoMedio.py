from aluno import Aluno

class AlunoEnsinoMedio(Aluno):
    nota_aprovacao = 6  

    def __init__(self, nome, idade, curso, numero_matricula, serie, nota1=0, nota2=0):
        super().__init__(nome, idade, curso, numero_matricula, nota1, nota2)
        self.__serie = serie

    # Getters e Setters
    def get_serie(self):
        return self.__serie
    
    def set_serie(self, serie):
        self.__serie = serie
