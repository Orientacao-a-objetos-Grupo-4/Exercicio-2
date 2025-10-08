from pessoa import Pessoa

class Aluno(Pessoa):

    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)
        self.curso = curso
        self.numero_matricula = 0
        self.__nota1 = 0
        self.__nota2 = 0

    
    # Getters
    def get_nota1(self):
        return self.__nota1
    
    def get_nota2(self):
        return self.__nota2
    
    def get_nota_aprovacao(self):
        return self.__nota_aprovacao
    
    # Setters
    def set_nota1(self, nota1):
        self.__nota1 = nota1

    def set_nota2(self, nota2):
        self.__nota2 = nota2

    def set_nota_aprovacao(self, nota_aprovacao):
        self.__nota_aprovacao = nota_aprovacao
    
    # Cálculo da média
    def calcular_media(self):
        return (self.__nota1 + self.__nota2) / 2
    
    # Impressão da situação
    def printar_situacao(self):
        media = self.calcular_media()
        if media >= self.__class__.__nota_aprovacao:
            print(f"O aluno {self.get_nome()}, matriculado no curso {self.curso}, foi aprovado com média: {media:.2f}")
        else:
            print(f"O aluno {self.get_nome()}, matriculado no curso {self.curso}, foi reprovado com média: {media:.2f}")
