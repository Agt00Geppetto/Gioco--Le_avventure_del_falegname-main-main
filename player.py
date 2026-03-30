import arcade
import os
from animazione import SpriteAnimato

SHEET_PATH = "./assets/Geppetto-sheet.png"

class Player(SpriteAnimato):

    DIREZIONI = ["su", "sinistra", "giu", "destra"]

    def __init__(self, scene):
        super().__init__()

        self.stato = None 
        self.shift_premuto = False
        self.salto = False

        self.vita = 100
        self.vita_massima = 100
        
        self.scene = scene
        self.center_x = 100
        self.center_y = 200
        self.scene.add_sprite("Player",self)

        # Variabili per il movimento e i salti
        self.jump_since_ground = 0
        self.max_jumps = 2
        self.physics_engine = None

        self.direzione = "giu"
        self.su = self.giu = self.sinistra = self.destra = False

    def set_physics_engine(self, engine):
        self.physics_engine = engine

    def move_left(self): 
        self.sinistra = True
        self.change_x = -5

    def run_left(self): 
        self.sinistra = True
        self.change_x = -10

    def move_right(self): 
        self.destra = True
        self.change_x = 5

    def run_right(self): 
        self.destra = True
        self.change_x = 10 

    def stop(self): self.change_x = 0

    def jump(self):
        if self.physics_engine and (self.physics_engine.can_jump() or self.jump_since_ground < self.max_jumps):
            self.physics_engine.jump(10)
            self.jump_since_ground += 1

    def update_jump_reset(self):
        if self.physics_engine and self.physics_engine.can_jump():
            self.jump_since_ground = 0
