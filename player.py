import arcade
import os
from animazione import SpriteAnimato

class Player(SpriteAnimato):

    DIREZIONI = ["su", "sinistra", "giu", "destra"]

    def __init__(self, scene):
        super().__init__()

        self.stato = None 
        self.shift_premuto = False

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

        self.direzione = "giu"
        self.su = self.giu = self.sinistra = self.destra = False

        self.setup()
        

    def setup(self):

        self.aggiungi_animazione(
            nome = "attack",
            percorso = "./assets/ATTACK 1.png",
            frame_width=96, frame_height=96,
            num_frame=7, colonne=7,
            durata=0.6,
            loop=False
        )
        self.aggiungi_animazione(
            nome = "idle",
            percorso = "./assets/IDLE.png",
            frame_width=96, frame_height=96,
            num_frame=10, colonne=10,
            durata=0.6,
            loop=True,
            default=True, # possiamo avere solo 1 animazione di default
        )
        self.aggiungi_animazione(
            nome = "run",
            percorso = "./assets/RUN.png",
            frame_width=96, frame_height=96,
            num_frame=16, colonne=16,
            durata=0.6,
            loop=True
        )
        self.aggiungi_animazione(
            nome = "hurt",
            percorso = "./assets/HURT.png",
            frame_width=96, frame_height=96,
            num_frame=4, colonne=4,
            durata=0.6,
            loop=False
        )
        self.aggiungi_animazione(
            nome = "walk",
            percorso = "./assets/WALK.png",
            frame_width=96, frame_height=96,
            num_frame=16, colonne=4,
            durata=1.5,
            loop=True
        )
        self.aggiungi_animazione(
            nome = "jump",
            percorso = "./assets/JUMP.png",
            frame_width=96, frame_height=96,
            num_frame=16, colonne=4,
            durata=0.6,
            loop=True
        )
        self.aggiungi_animazione(
            nome = "death",
            percorso = "./assets/DEATH.png",
            frame_width=96, frame_height=96,
            num_frame=9, colonne=3,
            durata=0.6,
            loop=True
        )


    def update_animation(self, delta_time: float = 1 / 60):
        dx = dy = 0
        if self.su:       
            dy += 4
        if self.giu:      
            dy -= 4
        if self.sinistra: 
            dx -= 4
        if self.destra:   
            dx += 4

        # da fare: capire in che direzione stiamo andando e impostare self.direzione

        if dx > 0:
            self.direzione = "destra"
        elif dx < 0:
            self.direzione = "sinistra"
        elif dy > 0:
            self.direzione = "su"
        elif dy < 0:
            self.direzione = "giu"
        
        # Scegliamo walk o idle

        if (dx != 0 or dy != 0) and self.shift_premuto:
            print("run")
            self.imposta_animazione("run")  
        elif (dx != 0 or dy != 0):
            print("walk")
            self.imposta_animazione("walk")           
        else:
            self.imposta_animazione("idle")

        super().update_animation(delta_time)

    # Metodi movimento
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
