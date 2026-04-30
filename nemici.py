import arcade
import random
from animazione import fungo
from animazione import occhio
from barra import BarraProgressiva

class Enemy(arcade.Sprite):

    def __init__(self, scene, danno, vita, vita_max, r_a, r_m, punteggio):
        super().__init__()

        self.vita = vita
        self.vita_massima = vita_max
        self.raggio_attacco = r_a
        self.raggio_movimento = r_m
        self.danno = danno
        self.scene = scene
        self.punteggio = punteggio

        self.barra_vita = BarraProgressiva(self.vita, self.vita_massima)

        self.stato = None
        self.timer_attacco = 0.0
        self.timer_danno = 0.0
        self.preso_danno = False


class Fungo(Enemy,fungo):

    def __init__(self, scene):
        
        Enemy.__init__(
            self = self,
            scene = scene, 
            danno = 15, 
            vita = 50, 
            vita_max = 50, 
            r_a = 75, 
            r_m = 450,
            punteggio = 100)

        fungo.__init__(self)

        coordinate_list_fungo = [[150, 125], [280, 125], [540, 125], [800, 125], [1060, 125], [1320, 125], [1580, 125], [1840, 125], [2100, 125], [2360, 125], [2620, 125], [2900, 125]]
        posizioni = random.sample(coordinate_list_fungo, k=3)

        for coordinate in posizioni:
            self.scene = scene
            self.position = coordinate
        self.scene.add_sprite("Enemy",self)

class Occhio(Enemy, occhio):
        
    def __init__(self, scene):

        Enemy.__init__(
            self = self,
            scene = scene, 
            danno = 20, 
            vita = 30, 
            vita_max = 30, 
            r_a = 50, 
            r_m = 450,
            punteggio = 150)
        
        occhio.__init__(self)

        coordinate_list_occhio = [[150, 300], [280, 309], [540, 318], [800, 327], [1060, 336], [1320, 345], [1580, 354], [1840, 363], [2100, 372], [2360, 381], [2620, 390], [2900, 400]]
        posizioni = random.sample(coordinate_list_occhio, k=2)

        for coordinate in posizioni:
            self.scene = scene
            self.position = coordinate
        self.scene.add_sprite("Enemy", self)