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
        self.center_y = 240
        self.scene.add_sprite("Player",self)

        # Variabili per il movimento e i salti
        self.jump_since_ground = 0
        self.max_jumps = 2
        self.physics_engine = None

        #Animazioni
        for i, dir in enumerate(self.DIREZIONI):
            self.aggiungi_animazione(f"idle_{dir}", SHEET_PATH,
                frame_width=288, frame_height=225, num_frame= 3, colonne= 3,
                durata=0.6, loop=True, default=(dir == "giu"), riga=i)
            self.aggiungi_animazione(f"walk_{dir}", SHEET_PATH,
                frame_width=288, frame_height=225, num_frame = 3, colonne= 3,
                durata=0.6, loop=True, riga=i)
            self.aggiungi_animazione(f"run_{dir}", SHEET_PATH,
                frame_width=288, frame_height=225, num_frame = 3, colonne= 3,
                durata=0.4, loop=True, riga=i)
            self.aggiungi_animazione(f"jump_{dir}", SHEET_PATH,
                frame_width=288, frame_height=225, num_frame = 3, colonne= 3,
                durata=0.6, loop=False, riga=i)
            self.aggiungi_animazione(f"attack_{dir}", SHEET_PATH,
                frame_width=288, frame_height=225, num_frame = 3, colonne= 3,
                durata=0.6, loop=False, riga=i)
            self.aggiungi_animazione(f"hurt_{dir}", SHEET_PATH,
                frame_width=288, frame_height=225, num_frame = 3, colonne= 3,
                durata=0.6, loop=False, riga=i)
            self.aggiungi_animazione(f"death_{dir}", SHEET_PATH,
                frame_width=288, frame_height=225, num_frame = 3, colonne= 3,
                durata=1.0, loop=True, riga=i)

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
