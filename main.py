from alunoEnsinoMedio import AlunoEnsinoMedio
from alunoGraduacao import AlunoGraduacao
from professor import Profressor


#Aprovados
aluno_medio = AlunoEnsinoMedio("João", 16, "Matemática", serie="2º", numero_matricula=123)
aluno_medio.set_nota1(8)
aluno_medio.set_nota2(7)

aluno_graduacao = AlunoGraduacao("Maria", 21, "Engenharia", numero_matricula=456, semestre="3º")
aluno_graduacao.set_nota1(6.5)
aluno_graduacao.set_nota2(7.5)

#Reprovados
aluno_medio2 = AlunoEnsinoMedio("João", 16, "Matemática", serie="2º", numero_matricula=123)
aluno_medio2.set_nota1(5)
aluno_medio2.set_nota2(4)

aluno_graduacao2 = AlunoGraduacao("Maria", 21, "Engenharia", numero_matricula=456, semestre="3º")
aluno_graduacao2.set_nota1(5)
aluno_graduacao2.set_nota2(4)


# Printar situação dos alunos
aluno_medio.printar_situacao()
aluno_graduacao.printar_situacao()

aluno_medio2.printar_situacao()
aluno_graduacao2.printar_situacao()

peofessor = Profressor("Joaquim", 40, "Doutorado")
print(peofessor)   