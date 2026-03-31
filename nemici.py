import arcade
import random
from animazione import enemy

class Enemy(enemy):

    def __init__(self, scene):
        super().__init__()

        self.vita_e1 = 50
        self.vita_massima_e1 = 50
        self.raggio_attacco = 100
        self.raggio_movimento = 450

        self.scene = scene
        self.center_x = 700
        self.center_y = 200
        self.scene.add_sprite("Enemy",self)

    def set_physics_engine(self, engine):

        self.physic_engine = engine

class Fungo(Enemy):

    pass

