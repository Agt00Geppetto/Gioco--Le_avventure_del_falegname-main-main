import arcade
import random

class Piattaforme:

    def __init__(self, scene):
        
        self.scene = scene
        self.crea_piattaforme()

    def crea_piattaforme(self):

        # Piattafroma base
        for x in range (200, 2800, 300):
            piattaforma = arcade.Sprite("./assets/piattaforma-new.png")
            piattaforma.center_x = x
            piattaforma.center_y = 180
            piattaforma.scale = 0.1
            self.scene.add_sprite("Piattaforme", piattaforma)

        # Piattaforme elaborate
        # for x in range (1001, 2000):
        # piattaforma_e = arcade.Sprite("./assets/piattaforma-elaborata.png")
        # piattaforma_e.center_x = 300
        # piattaforma_e.center_y = 200
        # piattaforma_e.scale = 0.5
        # self.scene.add_sprite("Piattaforme", piattaforma_e)