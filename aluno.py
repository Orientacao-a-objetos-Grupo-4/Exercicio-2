from pessoa import Pessoa

class Aluno(Pessoa):
    nota_aprovacao = 7  
    def __init__(self, nome, idade, curso, numero_matricula, nota1=0, nota2=0):
        super().__init__(nome, idade)
        self.__curso = curso
        self.__numero_matricula = numero_matricula
        self.__nota1 = nota1
        self.__nota2 = nota2

    # Getters
    def get_nota1(self):
        return self.__nota1
    
    def get_nota2(self):
        return self.__nota2
    
    def get_curso(self):
        return self.__curso
    
    def get_numero_matricula(self):
        return self.__numero_matricula
    
    # Setters
    def set_nota1(self, nota1):
        self.__nota1 = nota1

    def set_nota2(self, nota2):
        self.__nota2 = nota2

    def set_curso(self, curso):
        self.__curso = curso

    def set_numero_matricula(self, numero_matricula):
        self.__numero_matricula = numero_matricula
    
    # Cálculo da média
    def calcular_media(self):
        return (self.__nota1 + self.__nota2) / 2
    
    # Impressão da situação
    def printar_situacao(self):
        media = self.calcular_media()
        if media >= self.__class__.nota_aprovacao:
            print(f"✅ O aluno {self.get_nome()}, matriculado no curso {self.__curso}, foi aprovado com média: {media:.2f}")
        else:
            print(f"❌ O aluno {self.get_nome()}, matriculado no curso {self.__curso}, foi reprovado com média: {media:.2f}")
