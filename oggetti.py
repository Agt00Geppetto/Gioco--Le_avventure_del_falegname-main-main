import arcade
from barra import BarraProgressiva

class Oggetti(arcade.Sprite):
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

class Barile(Oggetti):

    def __init__(self, scene):

        Oggetti.__init__(
            self = self,
            scene = scene, 
            danno = 0, 
            vita = 20, 
            vita_max = 20, 
            r_a = 0, 
            r_m = 0,
            punteggio = 20)
        
        self.texture = arcade.load_texture("./assets/barile.png")
        self.scale = 0.4

class Secchio(Oggetti):

    def __init__(self, scene):

        Oggetti.__init__(
            self = self,
            scene = scene, 
            danno = 0, 
            vita = 10, 
            vita_max = 10, 
            r_a = 0, 
            r_m = 0,
            punteggio = 10)
        
        self.texture = arcade.load_texture("./assets/secchio.png")
        self.scale = 0.25


