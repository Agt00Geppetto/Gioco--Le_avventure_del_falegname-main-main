import arcade
import os
import random
#from inventario import Inventario
from player import Player
from muri import Muri
from nemici import Enemy
from pausa import PauseView
from barra import BarraProgressiva

class GameView(arcade.View):

    WORLD_WIDTH = 3000
    WORLD_HEIGHT = 3000
    SCREEN_WIDTH = 960
    SCREEN_HEIGHT = 540

    def __init__(self):
        super().__init__()
        
        self.p1 = None
        self.e1 = None

        self.physics_engine = None
        self.scene = None

        self.camera = None
        self.camera_ui = None

    def setup(self):
        self.scene = arcade.Scene()

        self.camera = arcade.Camera2D()
        self.camera_ui = arcade.Camera2D()

        self.p1 = Player(self.scene)

        self.barra = BarraProgressiva()

        self.e1 = Enemy(self.scene)

        self.muri = Muri(self.scene)

        self.physics_engine = arcade.PhysicsEnginePlatformer(
            player_sprite=self.p1,
            walls=self.scene["Walls"],
            gravity_constant=1.5,
        )

        self.p1.set_physics_engine(self.physics_engine)
        self.e1.set_physics_engine(self.physics_engine)

        self.physics_engine.enable_multi_jump(1)

        self.background = arcade.load_texture("./assets/sfondoG3.png")

        self.camera.position = (self.p1.center_x, self.p1.center_y)

    def on_draw(self):

        self.clear()
        
        self.camera_ui.use()
        arcade.draw_texture_rect(
            self.background,
            arcade.LBWH(
                0,
                0,
                self.SCREEN_WIDTH,
                self.SCREEN_HEIGHT
            )
        )

        self.barra.draw_barra()

        self.camera.use()
        self.scene.draw()

    def on_update(self, delta_time):

        self.scene.update(delta_time)
        self.p1.update_animation(delta_time)
        self.physics_engine.update()

        distanza = self.p1.position - self.e1.position

        if distanza > self.e1.raggio_attacco:
            self.e1.stato = "walk"
        else:
            self.e1.stato = "attack"


        self.aggiorna_camera()
        self.p1.update_jump_reset()
 
    def aggiorna_camera(self):
        # Prende la posizione corrente della camera (coordinate x e y)
        cam_x, cam_y = self.camera.position

        # Calcola la nuova posizione x della camera avvicinandola di 99% verso il centro del giocatore p1
        target_x = cam_x + (self.p1.center_x - cam_x) * 0.99
        # Calcola la nuova posizione y della camera avvicinandola di 99% verso il centro del giocatore p1
        target_y = cam_y + (self.p1.center_y - cam_y) * 0.99

        # Limita la posizione x della camera affinché non esca dai bordi del mondo di gioco
        target_x = max(self.SCREEN_WIDTH / 2, min(target_x, self.WORLD_WIDTH - self.SCREEN_WIDTH / 2))
        # Limita la posizione y della camera affinché non esca dai bordi del mondo di gioco
        target_y = max(self.SCREEN_HEIGHT / 2, min(target_y, self.WORLD_HEIGHT - self.SCREEN_HEIGHT / 2))

        # Aggiorna la posizione della camera con i valori calcolati
        self.camera.position = (target_x, target_y)

    def on_key_press(self, tasto, modificatori):

        if tasto == arcade.key.SPACE:
            self.p1.jump()
        elif tasto in (arcade.key.A, arcade.key.LEFT):
            self.p1.move_left()
            if modificatori & arcade.key.MOD_SHIFT:
                self.p1.run_left()
        elif tasto in (arcade.key.D, arcade.key.RIGHT):
            self.p1.move_right()
            if modificatori & arcade.key.MOD_SHIFT:
                self.p1.run_right()
        elif tasto == arcade.key.ESCAPE:
            pausa = PauseView(self)  # passiamo noi stessi per poter tornare in futuro, allo stato del gioco che avviene in questo momento
            self.window.show_view(pausa)

    def on_key_release(self, tasto, modificatori):

        if tasto in (arcade.key.A, arcade.key.D, arcade.key.RIGHT, arcade.key.LEFT):
            self.p1.stop()
        elif tasto == arcade.key.R:
            self.setup()