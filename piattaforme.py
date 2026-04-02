import arcade
import random

class Piattaforme:

    def __init__(self, scene):
        
        self.scene = scene
        self.crea_piattaforme()

    def crea_piattaforme(self):

        # Piattafroma base
        for x in range (200, 1000, 150):
            piattaforma = arcade.Sprite("./assets/piattaforma-new.png")
            piattaforma.center_x = x
            piattaforma.center_y = 180
            piattaforma.scale = 0.1
            self.scene.add_sprite("Piattaforme", piattaforma)