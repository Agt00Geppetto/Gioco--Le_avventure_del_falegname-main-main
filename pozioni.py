import arcade
import random

class Pozioni:

    def __init__(self, scene):
        
        self.scene = scene
        self.cura = "./assets/pozione_cura.png"
        self.valore_cura = 20
        self.pozioni_spawn()

    def pozioni_spawn(self):

        # Cura
        coordinate_list_b = [[200,150],[300,150],[550,150],[660,150],[1300,150],[1001,150],[1445,150],[1775,150],[2050,150],[2250,150],[2555,150],[2880,150]]
        posizioni = random.sample(coordinate_list_b, k=3) # il comando random.sample(), mi consente di scegliere nel mio caso 5 coordinate a caso che non si ripetono mai della lista coordinate_list_b

        for coordinate in posizioni:
            cura = arcade.Sprite(self.cura)
            cura.position = coordinate
            cura.scale = 0.1
            self.scene.add_sprite("Potions", cura)