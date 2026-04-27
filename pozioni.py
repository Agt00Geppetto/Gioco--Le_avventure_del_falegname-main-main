import arcade
import random

class Pozioni:

    def __init__(self, scene):
        
        self.scene = scene
        self.cura = 20
        self.pozioni_spawn()

    def pozioni_spawn(self):

        # Cura
        coordinate_list_b = [[200,95],[300,95],[550,95],[660,95],[1300,95],[1001,95],[1445,95],[1775,95],[2050,95],[2250,95],[2555,95],[2880,95]]
        posizioni = random.sample(coordinate_list_b, k=3) # il comando random.sample(), mi consente di scegliere nel mio caso 5 coordinate a caso che non si ripetono mai della lista coordinate_list_b

        for coordinate in posizioni:
            cura = arcade.Sprite("./assets/pozione_cura.png")
            cura.position = coordinate
            cura.scale = 0.1
            self.scene.add_sprite("Potions", cura)