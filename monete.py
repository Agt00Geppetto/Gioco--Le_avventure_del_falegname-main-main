import arcade 
import random

class Monete(arcade.Sprite):
    
    def __init__(self,scene):
        super().__init__()

        self.scene = scene
        self.genera_gioielli()
        
    def genera_gioielli(self):

        gioielli = ["monete", "lingotti"]
        probabilità = [60, 40]
        gioiello_estratto = random.choices(gioielli, weights = probabilità, k = 1)[0]

        # Monete estraibili
        if gioiello_estratto == "monete":
            opzioni =  ["./assets/moneta.png","./assets/moneta-corrotta.png"]
            pesi = [70, 30]
        # Lingotti estraibili
        elif gioiello_estratto == "lingotto":
            opzioni = ["./assets/lingotto.png","./assets/lingotto-corrotto.png"]
            pesi = [80, 20]

        gioiello = random.choices(opzioni, weights = pesi, k=1)[0]
