import arcade
import os
from animazione import player
from barra import BarraProgressiva

class Player(player):
    
    def __init__(self, scene):
        super().__init__()

        self.stato = None 
        self.shift_premuto = False
        self.salto = False
        self.raggio_attacco = 100
        self.corre = False
        self.attack_on = False
        self.preso_danno = False
        self.danno = 0.0

        self.vita = 100
        self.vita_massima = 100
        self.stamina = 50
        self.stamina_massima = 50

        self.barra_vita = BarraProgressiva(self.vita, self.vita_massima)
        self.barra_stamina = BarraProgressiva(self.stamina, self.stamina_massima)
        
        self.scene = scene
        self.center_x = 100
        self.center_y = 170
        self.scene.add_sprite("Player",self)

        # Variabili per il movimento e i salti
        self.jump_since_ground = 0
        self.max_jumps = 2
        self.physics_engine = None

    def set_physics_engine(self, engine):
        self.physics_engine = engine

    def move_left(self):
        self.attack_on = False 
        self.salto = False
        self.change_x = -3

    def run_left(self): 
        self.attack_on = False
        self.corre = True
        self.salto = False
        self.change_x = -5

    def move_right(self):
        self.attack_on = False
        self.salto = False
        self.change_x = 3

    def run_right(self): 
        self.attack_on = False
        self.corre = True
        self.salto = False
        self.change_x = 5

    def stop(self): 
        self.change_x = 0
        self.corre = False

    def attack(self):
        self.attack_on = True
        self.danno = 10.0

    def jump(self):
        if self.physics_engine and (self.physics_engine.can_jump() or self.jump_since_ground < self.max_jumps):
            self.physics_engine.jump(11.5)
            self.jump_since_ground += 1
        self.salto = True

    def update_jump_reset(self):
        if self.physics_engine and self.physics_engine.can_jump():
            self.jump_since_ground = 0

    def aggiorna_stamina(self, delta_time):
        if self.stamina == self.stamina_massima:
            return
        elif self.attack_on == False and self.corre == False:
            self.stamina += 5    
        elif self.stamina >= 0 and self.corre == True:
            self.stamina -=  1
        elif self.stamina >= 0 and self.attack_on == True:
            self.stamina -= 5