# Supondo que as classes já foram definidas conforme a versão anterior
# Aluno, AlunoEnsinoMedio e AlunoGraduacao

# Criação do aluno de ensino médio
from alunoEnsinoMedio import AlunoEnsinoMedio
from alunoGraduacao import AlunoGraduacao


aluno_medio = AlunoEnsinoMedio("João", 16, "Matemática", serie="2º")
aluno_medio.set_nota1(8)
aluno_medio.set_nota2(7)

# Criação do aluno de graduação
aluno_graduacao = AlunoGraduacao("Maria", 21, "Engenharia")
aluno_graduacao.set_nota1(6.5)
aluno_graduacao.set_nota2(7.5)

# Printar situação dos alunos
aluno_medio.printar_situacao()
aluno_graduacao.printar_situacao()
