import arcade 
import random

class Monete(arcade.Sprite):
    
    def __init__(self,scene):
        super().__init__()

        self.scene = scene
        self.genera_gioielli()
        
    def genera_gioielli(self):

        for x in range(200, 2900, 100):
            gioielli = ["monete", "lingotti"]
            probabilità = [60, 40]
            gioiello_estratto = random.choices(gioielli, weights = probabilità, k = 1)[0]

            # Monete estraibili
            if gioiello_estratto == "monete":
                opzioni =  ["./assets/moneta.png","./assets/moneta-corrotta.png"]
                pesi = [70, 30]
            # Lingotti estraibili
            elif gioiello_estratto == "lingotti":
                opzioni = ["./assets/lingotto.png","./assets/lingotto-corrotto.png"]
                pesi = [80, 20]

            risultato = random.choices(opzioni, weights = pesi, k=1)[0]

            gioiello = arcade.Sprite(risultato)
            gioiello.center_x = random.randint(200,2900)
            gioiello.center_y = random.randint(100,300)
            gioiello.scale = 0.05
            self.scene.add_sprite("Coins", gioiello)