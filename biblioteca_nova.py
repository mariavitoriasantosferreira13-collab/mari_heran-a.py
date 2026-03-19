from rich import print
from rich.panel import Panel

class Churrasco:
    def __init__(self, titulo, quant):
        self.titulo = titulo
        self.particpantes = quant
        
    def __str__(self):
        return f"Esse é {self.titiulo} com {self.participantes} pessoas participando"
    
    def analisar(self):
        conteudo = (f"Analisando [black] {self.titulo} com {self.particpantes} particpantes")
        painel = Panel(conteudo, title=self.titulo)
        print(painel)
        
c1 = Churrasco("Churras dos Amigos", 15)
c1.analisar()