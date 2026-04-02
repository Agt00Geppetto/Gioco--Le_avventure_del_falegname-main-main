import arcade
import random

class Muri:

    def __init__(self, scene):
        
        self.scene = scene
        self.crea_muri()
        
    def crea_muri(self):

        # Barile
        coordinate_list_b = [[200,95],[300,95],[550,95],[660,95],[1300,95],[1001,95],[1445,95],[1775,95],[2050,95],[2250,95],[2555,95],[2880,95]]
        posizioni = random.sample(coordinate_list_b, k=5) # il comando random.sample(), mi consente di scegliere nel mio caso 5 coordinate a caso che non si ripetono mai della lista coordinate_list_b

        for coordinate in posizioni:
            barile = arcade.Sprite("./assets/barile.png")
            barile.position = coordinate
            barile.scale = 0.4
            self.scene.add_sprite("Walls", barile)

        # Secchio
        coordinate_list_s = [[342, 80],[615, 80],[980, 80],[1245, 80],[1510, 80],[1730, 80],[2025, 80],[2290, 80],[2455, 80],[2680, 80],[2815, 80],[455, 80]]
        posizioni = random.sample(coordinate_list_s, k=3)

        for coordinate in posizioni:
            secchio = arcade.Sprite("./assets/secchio.png")
            secchio.position = coordinate
            secchio.scale = 0.25
            self.scene.add_sprite("Walls", secchio)

        # Terreno
        for x in range(-1000, 10000, 1000):
            terreno = arcade.Sprite("assets/Wood/Background layers/sfondo10.png")
            terreno.center_x = x
            terreno.center_y = 665
            terreno.scale = 1.8
            self.scene.add_sprite("Walls", terreno)


        # Portone (limite x, y)
        for y in range(200, 1000, 100):
            for x in range(-1000, 20, 65):
                portone = arcade.Sprite("./assets/portone.png")
                portone.center_y = y
                portone.center_x = x
                portone.scale = 1.5
                self.scene.add_sprite("Walls", portone)