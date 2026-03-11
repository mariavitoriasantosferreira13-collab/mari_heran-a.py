def lin():
    print("-"*40)

#exercício 1
# Observe o código.

# class Animal:
#     def falar(self):
# print("O animal faz um som")
# class Cachorro(Animal):
#     pass
# dog = Cachorro()
# dog.falar()
# Perguntas:
# 1. Qual é a classe pai?
# 2. Qual é a classe filha?
# 3. Por que o cachorro consegue usar o método falar()?

class Animal:
    def falar(self):
        print("O animal faz um som")
class Cachorro(Animal):
    def falar(self):
        print("Ocachorro faz au au!")
    pass

dog = Cachorro()
dog.falar()

#a) Animal
#b) cachorro
#c) porque ele herdou da Classe pai
lin()

#exercício 2
# Crie uma classe chamada Gato que herda da classe Animal.

# class Animal:
#     def falar(self):
#         print("O animal faz um som")
# class Gato(Animal):
#     pass
# g = Gato()
# g.falar()

# Pergunta:
# O método falar() foi criado na classe Gato ou herdado

class Animal:
    def falar(self):
        print("O animal faz um som")

class Gato(Animal):
    def falar(self):
        print("o gato falou miau!")
    pass

g = Gato()
g.falar()
#a) foi herdado

lin()

#exercício 3
# Complete o código para que o aluno possa acessar o atributo nome.

# class Pessoa:
#     def __init__(self, nome):
#         self.nome = nome

# class Aluno(Pessoa):
#     pass
# a = Aluno()
# print(a.nome)

# Perguntas:
# 1. Onde o atributo nome foi criado?
# 2. Por que a classe Aluno consegue usar esse atributo?

class Pessoa:
    def __init__(self, nome):
        self.nome = nome

class Aluno(Pessoa):
    def nome(self):
        return self.nome
    pass

a = Aluno("Maria")
print(a.nome)
#a) em Pessoa
#b) porque está herdando da Classe Pessoa

lin()

#exercício 4
# Complete o método da classe filha.

# class Animal:
#     def falar(self):
#         print("O animal faz um som")

# class Cachorro(Animal):
#     def falar(self):
#         print("Auau")

# dog = Cachorro()
# dog.falar()

# Desafio:
# Faça o cachorro falar "O cachorro late

class Animal:
    def falar(self):
        print("O animal faz um som")

class Cachorro(Animal):
    def falar(self):
        print("O cachorro late Auau")

dog = Cachorro()
dog.falar()

lin()

#exercício 5
# Crie uma classe filha chamada Moto que herda da classe Veiculo.

# class Veiculo:
#     def mover(self):
#         print("O veículo está se movendo")

# class Moto(Veiculo):
#     pass

# m = Moto()
# m.mover()

# Pergunta:
# A classe Moto criou o método mover() ou herdou?

class Veiculo:
    def mover(self):
        print("O veículo está se movendo")
class Moto(Veiculo):
    def mover(self):
        print("A moto está se movendo")
    pass


m = Moto()
m.mover()
#a) herdou

lin()

#exercício 6
# Crie uma classe pai chamada Pessoa.
# Depois crie duas classes filhas:
# Aluno
# Professor
# Aluno deve ter método estudar()
# Professor deve ter método ensinar()

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
class Aluno(Pessoa):
    def estudar(self):
        return(f"{self.nome} está estudando")

class Professor(Pessoa):
    def ensinar(self):
        return(f"{self.nome} está ensinando")
    
a = Aluno("Lucas", 20)
p = Professor("Mirela", 35)

print(a.estudar())
print(p.ensinar())

lin()

#exercício 7
# Crie uma classe pai chamada Animal com atributo nome.
# Depois crie duas classes filhas:
# Cachorro
# Gato
# Cada classe deve ter seu próprio método falar().

class Animal():
    def __init__(self, nome):
        self.nome = nome

class Cachorro(Animal):
    def falar(self):
        print("O cachorro fala au au!")

class Gato(Animal):
    def falar(self):
        print("O gato fala miau!")
c1 = Cachorro("nick")
g1 = Gato("Apolo")

c1.falar()
g1.falar()

lin()

#exercício 8
# Complete o código usando herança.
# class Pessoa:
#     def __init__(self, nome):
#         self.nome = nome

# class Professor(Pessoa):
#     def ensinar(self):
#         print(self.nome, "está ensinando")

# Crie um objeto Professor e chame o método ensinar().

class Pessoa:
    def __init__(self, nome):
        self.nome = nome

class Professor(Pessoa):
    def ensinar(self):
        print(self.nome, "está ensinando")

p1 = Professor("Bruno")
p1.ensinar()

lin()

#exercício 9
# Crie uma classe pai chamada Veiculo com:
# atributo marca
# método mover()
# Depois crie duas classes filhas:
# Carro
# Moto
# Cada uma deve imprimir uma mensagem diferente ao se mover.

class Veiculo:
    def __init__(self, marca):
        self.marca = marca

def mover(self):
        print(f"O Veículo da Marca {self.marca} está se movendo")

class Carro(Veiculo):
    def mover(self):
        print(f"O Carro da marca {self.marca} está se movendo para trás")

class Moto(Veiculo):
    def mover(self):
        print(f"A moto da marca {self.marca} está se movendo para frente")

carro1 = Carro("toyota")
moto1 = Moto("Honda")

carro1.mover()
moto1.mover()

lin()

#exercício 10
# Crie uma classe chamada Personagem com:
# atributo nome
# método atacar()
# Depois crie duas classes filhas:
# Guerreiro
# Mago
# Cada personagem deve atacar de forma diferente.
# Exemplo de saída esperada:
# Thor ataca com espada
# Merlin lança magia
# Classe pai → define características gerais
# Classe filha → herda essas características e pode modificá-las

class Personagem:
    def __init__(self, nome):
        self.nome = nome

    def atacar(self):
        print(f"{self.nome}, atacou com espada")

class Guerreiro(Personagem):
    def atacar(self):
        print(f"{self.nome}, atacou com espada ")

class Mago(Personagem):
    def atacar(self):
        print(f"{self.nome}, lança magia ")

per1 = Guerreiro("Klaus")
per2 = Mago("Harry")

per1.atacar()
per2.atacar()


