import arcade
import random
from animazione import SpriteAnimato

class Enemy(SpriteAnimato):

    def __init__(self, scene):
        super().__init__()

        self.vita_e1 = 50
        self.vita_massima_e1 = 50
        self.raggio_attacco = 20

        self.scene = scene
        self.center_x = 400
        self.center_y = 240
        self.scene.add_sprite("Enemy",self)

    def set_physics_engine(self, engine):

        self.physics_engine = engine

class Fungo(Enemy):

    pass

