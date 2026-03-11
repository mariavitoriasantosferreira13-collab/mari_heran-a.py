class Pessoa:
    def __init__(self, nome):
        self.nome = nome

class Aluno(Pessoa):
    def nome(self):
        return self.nome
    pass