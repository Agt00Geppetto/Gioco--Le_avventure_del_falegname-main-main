import arcade
import arcade.future.background as background
import os
import random
#from inventario import Inventario
from player import Player
from muri import Muri
from piattaforme import Piattaforme
from nemici import Fungo
from nemici import Occhio
from pausa import PauseView
from sfondo import ParallaxBackground
from monete import Monete

class Gioco(arcade.View):

    WORLD_WIDTH = 3000
    WORLD_HEIGHT = 3000
    SCREEN_WIDTH = 960
    SCREEN_HEIGHT = 540
    CAMERAA_SPEED = 0.1

    def __init__(self):
        super().__init__()
        
        self.p1 = None
        self.fungo = None
        self.occhio = None
        self.punteggio = 0

        self.physics_engine = None
        self.scene = None

        self.camera = None
        self.camera_ui = None
        self.timer: float = 0.0

    def setup(self):

        self.scene = arcade.Scene()

        self.camera = arcade.Camera2D()
        self.camera_ui = arcade.Camera2D()

        self.p1 = Player(self.scene)
        self.sfondo = ParallaxBackground()
        # self.scene.add_sprite_list_after("Player", "Foreground")

        self.soldi = Monete(self.scene) 

        self.fungo = Fungo(self.scene)
        self.occhio = Occhio(self.scene)

        self.muri = Muri(self.scene)
        self.piattaforme = Piattaforme(self.scene)

        self.physics_engine = arcade.PhysicsEnginePlatformer(
            player_sprite = self.p1,
            walls = self.scene["Walls"],
            platforms = self.scene["Piattaforme"],
            gravity_constant = 1.5,
        )

        # self.physic_engine = arcade.PhysicsEngineSimple(
        #     player_sprite = self.fungo,
        #     walls = self.scene["Walls"]
        # )

        self.p1.set_physics_engine(self.physics_engine)

        self.physics_engine.enable_multi_jump(1)

        self.camera.position = (self.p1.center_x, self.p1.center_y)


    def update_animation(self):

        if (self.p1.change_x != 0 or self.p1.change_y != 0) and self.p1.corre == False:
             self.p1.imposta_animazione("walk")
        elif (self.p1.change_x != 0 or self.p1.change_y != 0) and self.p1.corre == True:
             self.p1.imposta_animazione("run")
        elif self.p1.salto == True and not self.p1.physics_engine.can_jump():
            self.p1.imposta_animazione("jump")
        elif self.p1.attack_on == True:
            print("attack")
            self.p1.imposta_animazione("attack")           
        else:
             self.p1.imposta_animazione("idle")

    def aggiorna_camera(self):

        cam_x, cam_y = self.camera.position

        # Lerp verso il player
        target_x = cam_x + (self.p1.center_x - cam_x) * 0.1
        target_y = cam_y + (self.p1.center_y - cam_y) * 0.1

        # Clamping ai bordi
        target_x = max(self.SCREEN_WIDTH / 2, min(target_x, self.WORLD_WIDTH - self.SCREEN_WIDTH / 2))
        target_y = max(self.SCREEN_HEIGHT / 2, min(target_y, self.WORLD_HEIGHT - self.SCREEN_HEIGHT / 2))

        self.camera.position = (target_x, target_y)

    def on_draw(self):
        
        self.clear()
        self.camera.use()
        self.sfondo.draw(self.camera)

        self.scene.draw()

        self.camera_ui.use()
        self.p1.barra_vita.draw_barra()
        arcade.draw_text(
            x = 480,
            y = 25,
            text = f"Il tuo punteggio è di:{self.punteggio}",  
            color = arcade.color.WHITE, 
            font_size = 10,
            font_name = ("./assets/d_i_y_75/D.I.Y.'75.ttf"),
            bold = True 
            )

    def on_update(self, delta_time):

        self.scene.update(delta_time)
        self.aggiorna_camera()
        self.p1.update_animation(delta_time)
        self.physics_engine.update()

        self.p1.update_jump_reset()

        collisioni = arcade.check_for_collision_with_list(self.p1, self.soldi.scene["Coins"])

        for soldi in collisioni:
            self.punteggio += 20
            soldi.kill()
        
        distanza = self.p1.center_x - self.fungo.center_x 

        if distanza > self.fungo.raggio_movimento or distanza < -self.fungo.raggio_movimento:
            self.fungo.imposta_animazione("idle")
            self.fungo.change_x = 0
        elif distanza < self.fungo.raggio_attacco and distanza >= -self.fungo.raggio_movimento:
            self.fungo.change_x = -3
        elif distanza <= self.fungo.raggio_movimento and distanza > -self.fungo.raggio_attacco:
            self.fungo.change_x = 3
        elif distanza <= self.fungo.raggio_attacco or distanza >= -self.fungo.raggio_attacco:
            self.fungo.imposta_animazione("attack")
            self.fungo.change_x = 0
            self.fungo.change_y = 0
            self.timer += delta_time
            if self.timer == 1:
                self.p1.vita -= 5
                self.p1.imposta_animazione("hurt")
                self.timer -= 1
        if distanza <= self.p1.raggio_attacco and distanza >= -self.p1.raggio_attacco and self.p1.attack_on == True:
            self.fungo.imposta_animazione("hurt")
            self.fungo.vita -= self.p1.danno
            print("vita_fungo")
        elif self.fungo.vita == 0:
            self.fungo.imposta_animazione("death")

        if self.p1.change_x < 0: 
            self.p1.scale = (-2.0, 2.0)
        elif self.p1.change_x > 0:
            self.p1.scale = (2.0, 2.0)
        
        if self.fungo.change_x < 0: 
            self.fungo.scale = (-2.0, 2.0)
        elif self.fungo.change_x > 0:
            self.fungo.scale = (2.0, 2.0)

        if self.occhio.change_x < 0: 
            self.occhio.scale = (-2.0, 2.0)
        elif self.occhio.change_x > 0:
            self.occhio.scale = (2.0, 2.0)

        self.update_animation()

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
        elif tasto == arcade.key.E:
            self.barra -= self.p1.danno

    def on_key_release(self, tasto, modificatori):

        if tasto in (arcade.key.A, arcade.key.D, arcade.key.RIGHT, arcade.key.LEFT):
            self.p1.stop()
        elif tasto == arcade.key.R:
            self.setup()
