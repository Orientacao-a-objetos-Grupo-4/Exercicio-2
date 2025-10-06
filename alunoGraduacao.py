from aluno import Aluno

class AlunoEnsinoMedio(Aluno):
    def __init__(self, nome, idade, curso, semestre):
        super().__init__(nome, idade, curso)
        self.semestre = semestre
    
    def setSemestre(self, semestre):
        self.semestre = semestre

    def getSemestre(self):
        return self.semestre

    def printarSituacao(self, aprovado):
        media = self.calcular_media()
        if aprovado:
            print(f"O aluno {self.getNome()}, matriculado no semestre {self.getSemestre()}, foi aprovado com média: {media:.2f}")
        else:
            print(f"O aluno {self.getNome()}, matriculado no semestre {self.getSemestre()}, foi reprovado com média: {media:.2f}")

    def verificar_aprovado(self):
        media = self.calcular_media()
        aprovado = media >= 6
        self.printarSituacao(aprovado)
        return aprovado
