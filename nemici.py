import arcade
import random
from animazione import fungo
from animazione import occhio
from barra import BarraProgressiva

class Enemy(arcade.Sprite):

    def __init__(self, scene, danno, vita, vita_max, r_a, r_m):
        super().__init__()

        self.vita = vita
        self.vita_massima = vita_max
        self.raggio_attacco = r_a
        self.raggio_movimento = r_m
        self.danno = danno
        self.scene = scene

        self.barra_vita = BarraProgressiva(self.vita, self.vita_massima, entità = self)


class Fungo(Enemy,fungo):

    def __init__(self, scene):
        
        Enemy.__init__(
            self = self,
            scene = scene, 
            danno = 15, 
            vita = 50, 
            vita_max = 50, 
            r_a = 100, 
            r_m = 450)

        fungo.__init__(self)

        self.scene = scene
        self.center_x = 700
        self.center_y = 125
        self.scene.add_sprite("Enemy",self)

class Occhio(Enemy, occhio):
        
    def __init__(self, scene):

        Enemy.__init__(
            self = self,
            scene = scene, 
            danno = 20, 
            vita = 30, 
            vita_max = 30, 
            r_a = 75, 
            r_m = 450)
        
        occhio.__init__(self)

        self.scene = scene
        self.center_x = 800
        self.center_y = 400
        self.scene.add_sprite("Enemy", self)