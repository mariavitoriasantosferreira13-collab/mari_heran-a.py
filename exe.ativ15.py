def lin():
       print("-"*40)

#exercício 1
class Animal: 
 
    def __init__(self, nome): 
        self.nome = nome 
 
class Cachorro(Animal): 
 
    def __init__(self, nome, raca):
     self.nome = nome 
     self.raca = raca
 
c = Cachorro("Bolt", "Labrador") 
print(c.nome) 
print(c.raca)

lin()

#exercício 2
class Conta: 
 
    def __init__(self, saldo): 
        self._saldo = saldo 
 
    def sacar(self, valor): 
        if valor <= self._saldo: 
            self._saldo -= valor 
 
conta = Conta(1000) 
print(conta._saldo) 

lin()

#exercício 3
class Pessoa: 
 
    def __init__(self, nome): 
        self.nome = nome 
 
class Professor(Pessoa): 
 
    def __init__(self, nome, disciplina): 
        super().__init__(nome)
        self.disciplina = disciplina 
 
p = Professor("Ana", "Programação") 
print(p.nome) 
print(p.disciplina)

lin()

#exercício 4
class Animal: 
 
    def falar(self): 
        print("Som") 
 
class Gato(Animal): 
 
    def falar(self): 
        print("Miau") 
 
class Cachorro(Animal): 
 
    def falar(self): 
        print("Au au") 
 
animais = [Gato(), Cachorro()] 
 
for a in animais: 
    a.falar() 

lin()

#exercício 5

class Produto: 
 
    def __init__(self, preco): 
        self.__preco = preco 
 
    def get_preco(self, valor): 
        if valor > 0: 
          self.__preco = valor 
 
    def set_preco(self): 
        return self.__preco 
 
p = Produto(50) 
p.get_preco(100) 
print(p.set_preco())

lin()

#exercício 6

class Animal: 
 
    def __init__(self, nome): 
        self.nome = nome 
 
class Vaca(Animal): 
 
    def falar(self): 
        return(self.nome, "faz muuu") 
 
v = Vaca("Mimosa") 
print(v.falar())

lin()

#exercício 7

class Conta: 
 
    def __init__(self, saldo): 
        self._saldo = saldo 
 
    def depositar(self, valor): 
        if valor > 0: 
            self._saldo += valor 

    def get_saldo(self):
        return self._saldo

 
conta = Conta(1000) 
conta.depositar(500) 
print(conta.get_saldo()) 

lin()

#exercício 8

class Animal: 
 
    def falar(self): 
        print("Som") 
 
class Pato(Animal): 
 
    def falar(self): 
        print("Quack") 
 
p = Pato() 
p.falar()

lin()

#exercício 9

class Pessoa: 
 
    def __init__(self, nome): 
        self.nome = nome 
 
class Aluno(Pessoa): 
 
    def estudar(self): 
        print(self.nome, "está estudando") 
 
a = Aluno("Lucas") 
a.estudar()

lin()

#exercício 10

class Animal: 
 
    def __init__(self, nome): 
        self.nome = nome 

    def falar(self): 
        print("faz som") 
 
class Cachorro(Animal): 
 
    def __init__(self, nome): 
        super().__init__(nome) 
        print(f"{self.nome} faz au au ")
 
 
animais = [ 
Cachorro("Bolt"), 
Animal("Bicho") 
] 
 
for a in animais: 
    a.falar() 
    
lin()

#exercício 11

class Produto: 
 
    def __init__(self, preco): 
        self.__preco = preco 


 
p = Produto(100) 
p.__preco = -200 
print(p.__preco) 

lin()

#exercício 12
class Animal: 

    def __init__(self, nome):
        self.nome = nome
 
    def falar(self): 
        print("Som") 
 
class Gato(Animal): 
 
    def falar(self): 
        print(f"{self.nome} faz Miau") 
 
class Cachorro(Animal): 
 
    def falar(self): 
        print(f"{self.nome} faz Au au") 
 
animais = [Gato("Fred"), Cachorro("Nick")] 
 
for a in animais: 
    a.falar() 
 
lin()

#exercício 13
class Conta: 
 
    def __init__(self, saldo): 
        self.__saldo = saldo 
 
    def sacar(self, valor): 
        if valor <= self.__saldo: 
            self.__saldo -= valor 

    def exibir(self):
        return self.__saldo
 
c = Conta(500) 
c.sacar(100) 
print(c.exibir())

lin()

#exercíccio 14
class Animal: 
 
    def __init__(self, nome): 
        self.nome = nome 
 
class Gato(Animal): 
 
    def falar(self): 
        print(self.nome, "mia") 
 
g = Gato("Luna") 
g.falar() 

lin()

#exercício 15

class Pessoa: 
 
    def __init__(self, nome): 
        self.nome = nome 
 
class Professor(Pessoa): 
 
    def ensinar(self): 
        print(self.nome, "ensina") 
 
prof = Professor("Pedro") 
prof.ensinar() 

lin()

#Exercício 16
class Animal: 

    def __init__(self, nome):
        self.nome = nome
 
    def falar(self): 
        print("Som") 
 
class Gato(Animal): 
 
    def miar(self): 
        print(f"{self.nome} faz Miau") 
 
g = Gato("mike") 
g.miar()

lin()

#exercício 17

class Conta: 
    def __init__(self, saldo): 
        self.__saldo = saldo 
        
    def set_saldo(self, valor): 
        if valor >= 0: 
            self.__saldo = valor

    def get_saldo(self):
        return self.__saldo

c = Conta(100) 
c.set_saldo(-50) 
print(c.get_saldo())

lin()

#exercício 18

class Animal: 

    def falar(self): 
        print("Som") 

class Cachorro(Animal): 
    def falar(self): 
        print("O Cachorro faz au au") 

class Gato(Animal): 
     def falar(self): 
        print("o Gato faz miau miau") 
pass 

Animais = [Cachorro(), Gato()] 
for a in Animais: 
    a.falar()

lin()

#exercício 19

class Produto:
    def __init__(self, preco):
        self.__preco = preco

    def set_preco(self, valor):
        if valor > 0:
            self.__preco = valor

    def get_preco(self):
        return self.__preco


p = Produto(100)
p.set_preco(-200)
print(p.get_preco())

lin()

#exercício 20
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        print("Som")


class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome)
        self.raca = raca

    def falar(self):
        super().falar()
        print(f"{self.nome} faz Au au")


animais = [
    Cachorro("Bolt", "Labrador"),
    Animal("Bicho")
]

for a in animais:
    a.falar()

lin()

#exercício 21
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        print("Som de animal")


class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome)
        self.raca = raca

    def falar(self):
        print(self.nome, "late")


class Gato(Animal):
    def falar(self):
        print(self.nome, "mia")

class Vaca(Animal):
    def falar(self):
        print(self.nome, "faz muuu")


class Conta:
    def __init__(self, saldo):
        self.__saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor

    def get_saldo(self):
        return self.__saldo


animais = [
    Cachorro("Bolt", "Labrador"),
    Gato("Luna"),
    Vaca("Estrela")
]

for a in animais:
    a.falar()


conta = Conta(1000)
conta.depositar(500)
conta.sacar(200)

print("Saldo:", conta.get_saldo())

conta.depositar(500)
conta.sacar(200)

print("Saldo final:", conta.get_saldo())

lin()

#exercício 22
class Animal: 
    def __init__(self, nome): 
        self.nome = nome 

    def falar(self): 
        print("O animal faz um som") 

class Cachorro(Animal): 

    def __init__(self, nome, raca): 
        super().__init__(nome) 
        self.raca = raca

    def falar(self): 
        print(f"{self.nome}, late")

class Gato(Animal): 
    def falar(self): 
        print(f"{self.nome}, mia") 

class Conta: 
    def __init__(self, saldo): 
        self.__saldo = saldo 

    def depositar(self, valor): 
        if valor > 0 :
            self.__saldo += valor 

    def sacar(self, valor): 
        if valor <= self.__saldo:
               self.__saldo -= valor 

    def get_saldo(self): 
        return self.__saldo

animais = [ 
    Cachorro("Bolt", "Labrador"), 
    Gato("Luna") 
] 
for a in animais:
 a.falar() 

conta = Conta(1000) 
conta.depositar(500) 
conta.sacar(200) 
print(conta.get_saldo())

lin()

#exercício 23

class Produto:
    def __init__(self, preco):
        self._preco = preco
    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor ):
        if self.valor > 0:
            self._preco = self.valor

p = Produto(50)
print(p.preco)

lin()

#exercício 24

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        print("Som de animal")


class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome)
        self.raca = raca

    def falar(self):
        print(self.nome,"late")

class Gato(Animal):
    def falar(self):
        print(self.nome, "mia")

class Vaca(Animal):
    def falar(self):
        print(self.nome, "faz muuu")

class Conta: 
    def __init__(self, saldo):
        self.__saldo = saldo 

    def depositar(self, valor): 
        if valor > 0 :
            self.__saldo += valor 

    def sacar(self, valor): 
        if valor <= self.__saldo: 
            self.__saldo -= valor

    def get_saldo(self): 
        return self.__saldo 

class Produto: 
    def __init__(self, preco): 
        self._preco = preco

    @property 
    def preco(self): 
        return self._preco
     
    @preco.setter 
    def preco(self, valor): 
        if valor > 0: 
            self._preco = valor

animais = [ 
    Cachorro("Bolt", "Labrador"), 
    Gato("Luna"), 
    Vaca("Estrela") 
]

for a in animais: 
    a.falar()

conta = Conta(1000) 
conta.depositar(500) 
conta.sacar(200)
print("Saldo:", conta.get_saldo())

p = Produto(100) 
p.preco = 200 
print(p.preco)

# Tarefa dos estudantes

# Peça para eles responderem:

# 1. Quantos erros existem no código?
#8 erros

# 2. Onde está o erro de herança?
#na classe Cachorro

# 3. Onde está o erro de super() ou falta dele?
#Na classe Cachorro, porque está criando um novo atributo, por isso é pra usar o super()

# 4. Onde está o erro de encapsulamento?
#No def preco estava: self.preco, mas era pra ser self._preco

# 5. Onde está o erro de getter?
#Na classe Produto

# 6. Onde está o erro de property?
#Estava escrito apenas return preco, mas era pra ser return self._preco

# 7. Onde está o erro de polimorfismo?
#Na classe Cachorro, no print, faltava o self