import arcade
import os
from animazione import SpriteAnimato

class Player(SpriteAnimato):
    DIREZIONI = ["su", "sinistra", "giu", "destra"]

    def __init__(self, scene):
        super().__init__(scala = 2.0)

        self.scene = scene
        # Variabili per il movimento e i salti
        self.jump_since_ground = 0
        self.max_jumps = 2
        self.physics_engine = None

        for i, dir in enumerate(self.DIREZIONI):
            self.aggiungi_animazione(f"idle_{dir}", "./assets/IDLE.png",
                frame_width=64, frame_height=64, num_frame=10, colonne=1,
                durata=0.8, loop=True, default=(dir == "giu"), riga=i)
            self.aggiungi_animazione(f"walk_{dir}", "./assets/RUN.png",
                frame_width=64, frame_height=64, num_frame=16, colonne=1,
                durata=1.0, loop=True, riga=i)

        self.direzione = "giu"
        self.su = self.giu = self.sinistra = self.destra = False

    def setup(self):
        p1 = arcade.Sprite("./assets/IDLE1.png")
        p1 = SpriteAnimato(scale = 1.5)
        p1.aggiungi_animazione(
            nome = "attack",
            percorso = "./assets/ATTACK 1.png",
            frame_width=64, frame_height=64,
            num_frame=7, colonne=1,
            durata=0.6,
            loop=False
        )
        p1.aggiungi_animazione(
            nome = "idle",
            percorso = "./assets/IDLE.png",
            frame_width=64, frame_height=64,
            num_frame=10, colonne=1,
            durata=0.6,
            loop=True,
            default=True, # possiamo avere solo 1 animazione di default
        )
        p1.aggiungi_animazione(
            nome = "run",
            percorso = "./assets/RUN.png",
            frame_width=64, frame_height=64,
            num_frame=16, colonne=1,
            durata=0.6,
            loop=False
        )
        p1.aggiungi_animazione(
            nome = "hurt",
            percorso = "./assets/HURT.png",
            frame_width=64, frame_height=64,
            num_frame=4, colonne=1,
            durata=0.6,
            loop=False
        )
        p1.aggiungi_animazione(
            nome = "walk",
            percorso = "./assets/RUN.png",
            frame_width=64, frame_height=64,
            num_frame=16, colonne=1,
            durata=1.0,
            loop=False
        )

        self.center_x = 100
        self.center_y = 240
        self.scene.add_sprite("Player", p1)

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

        # Scegliamo walk o idle
        if dx != 0 or dy != 0:
            self.imposta_animazione(f"walk_{self.direzione}")
        else:
            self.imposta_animazione(f"idle_{self.direzione}")

        super().update_animation(delta_time)

    # Metodi movimento
    def set_physics_engine(self, engine):
        self.physics_engine = engine

    def move_left(self): self.change_x = -5

    def run_left(self): self.change_x = -10

    def move_right(self): self.change_x = 5

    def run_right(self): self.change_x = 10

    def stop(self): self.change_x = 0

    def jump(self):
        if self.physics_engine and (self.physics_engine.can_jump() or self.jump_since_ground < self.max_jumps):
            self.physics_engine.jump(10)
            self.jump_since_ground += 1

    def update_jump_reset(self):
        if self.physics_engine and self.physics_engine.can_jump():
            self.jump_since_ground = 0
