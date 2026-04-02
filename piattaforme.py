import arcade
import random

class Piattaforme:

    def __init__(self, scene):
        
        self.scene = scene
        self.crea_piattaforme()

    def crea_piattaforme(self):

        # Piattafroma base
        coordinate_list_p = [[245, 230],[480, 230],[715, 230],[990, 230],[1210, 230],[1455, 230],[1780, 230],[2020, 230],[2345, 230],[2510, 230],[2735, 230],[2895, 230]]
        posizioni = random.sample(coordinate_list_p, k=6)

        for coordinate in posizioni:
            piattaforma = arcade.Sprite("./assets/piattaforma-new.png")
            piattaforma.position = coordinate
            piattaforma.scale = 0.1
            self.scene.add_sprite("Piattaforme", piattaforma)

        # Piattaforme elaborate
        #for x in range (1001, 2000):
        # piattaforma_e = arcade.Sprite("./assets/piattaforma-elaborata.png")
        # piattaforma_e.center_x = 300
        # piattaforma_e.center_y = 180
        # piattaforma_e.scale = 0.75
        # self.scene.add_sprite("Piattaforme", piattaforma_e)