class Veiculo:
    def __init__(self,marca):
        self.marca = marca

    def mover(self):
        print("O carro está se movendo")

class Carro(Veiculo):
    def mover(self):
        print(f"O Carro da {self.marca} está se movendo")

car1 = Carro("Renault")
car1.mover()

#ativ