import abc

class pessoa(abc.ABC):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
