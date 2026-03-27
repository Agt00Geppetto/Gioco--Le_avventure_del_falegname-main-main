import arcade
import random
from animazione import SpriteAnimato

class Enemy(SpriteAnimato):

    DIREZIONI = ["su", "sinistra", "giu", "destra"]

    def __init__(self, scene):
        super().__init__()

        self.stato = None

        self.vita_e1 = 50
        self.vita_massima_e1 = 50

        self.scene = scene
        self.center_x = 100
        self.center_y = 240
        self.scene.add_sprite("Enemy",self)

        self.direzione = "giu"
        self.su = self.giu = self.sinistra = self.destra = False

        self.setup()

    def setup(self):

        self.aggiungi_animazione(
            nome = "attack",
            percorso = "./assets/ATTACK-e1.png",
            frame_width=60, frame_height=40,
            num_frame=5, colonne=5,
            durata=0.6,
            loop=False
        )
        self.aggiungi_animazione(
            nome = "walk",
            percorso = "./assets/WALK-e1.png",
            frame_width=60, frame_height=40,
            num_frame=6, colonne=6,
            durata=0.6,
            loop=False
        )

        self.aggiungi_animazione(
            nome = "death",
            percorso = "./assets/DEATH-e1.png",
            frame_width=60, frame_height=40,
            num_frame=4, colonne=4,
            durata=0.6,
            loop=False
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
        if dx != 0 or dy != 0:
            self.imposta_animazione("walk")
        else:
            self.imposta_animazione("attack")

        super().update_animation(delta_time)


    def set_physics_engine(self, engine):

        self.physics_engine = engine

    def movimento(self):


