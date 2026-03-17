def lin():
    print("-"*40)


class Animal:
    def __init__(self, nome):
        self.nome = nome 

    def som(self):
        print("O Animal faz um som")

class Dog(Animal):

    def som(self):
        print(f"O Dog {self.nome} faz au au!!")


class Cat(Animal):
    def som(self):
        print(f"O Cat {self.nome} faz miau miau!!")


Dog1 = Dog("Mike")
Cat1 = Cat("Fred")
Dog1.som()
Cat1.som()

lin()

class Animal:
    def __init__(self, nome):
        self.nome = nome 

    def som(self):
        return("O Animal faz um som")

class Dog(Animal):
    def som(self):
        return(f"O Dog {self.nome} faz au au!!")

class Cat(Animal):
    def som(self):
        return(f"O Cat {self.nome} faz miau miau!!")
    
Dog1 = Dog("Mike")
Cat1 = Cat("Fred")
print(Dog1.som())
print(Cat1.som())

lin()

#teste1

