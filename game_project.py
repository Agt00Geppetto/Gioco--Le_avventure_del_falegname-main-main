import arcade
import os
import random
#from inventario import Inventario
from player import Player
from muri import Muri
from nemici import Enemy
#from barra_vita import Barra

class GameView(arcade.Window):
    #impaginazione globale
    WORLD_WIDTH : int = 3000
    WORLD_HEIGHT : int = 3000
    SCREEN_WIDTH : int = 960
    SCREEN_HEIGHT : int = 540

    def __init__(self, width, height, title):
        super().__init__(width, height, title, fullscreen=True,)

        #sprites
        self.p1 = None
        self.e1 = None
        self.barile = None
        self.secchio = None

        #fisica del gioco (base)
        self.pyshics_engine = None
        self.scene = None

        self.camera = None
        self.camera_ui = None

        self.setup()

    def aggiorna_camera(self):
        cam_x, cam_y = self.camera.position

        # Lerp verso il player
        target_x = cam_x + (self.p1.center_x - cam_x) * 0.1
        target_y = cam_y + (self.p1.center_y - cam_y) * 0.1

        # Clamping ai bordi
        target_x = max(self.SCREEN_WIDTH / 2, min(target_x, self.WORLD_WIDTH - self.SCREEN_WIDTH / 2))
        target_y = max(self.SCREEN_HEIGHT / 2, min(target_y, self.WORLD_HEIGHT - self.SCREEN_HEIGHT / 2))

        self.camera.position = (target_x, target_y)


    def setup(self):

        #metodo per riassumere tutte le Spritelist di arcade   
        #prinicpali sprites da far collidere col giocatore (oltre al giocatore stesso)     
        self.scene = arcade.Scene()

        self.camera = arcade.Camera2D()
        self.camera_ui = arcade.Camera2D()
        
        self.p1 = Player()
        self.p1.center_x = 100
        self.p1.center_y = 240
        self.scene.add_sprite("Player", self.p1)

        self.e1 = Enemy("./assets/Legnamorta.png", 0.8)
        self.e1.center_x = 800
        self.e1.center_y = 350
        self.scene.add_sprite("Enemy", self.e1)

        self.muri = Muri(self.scene)

        self.physics_engine = arcade.PhysicsEnginePlatformer(
            player_sprite = self.p1,
            walls = self.scene["Walls"],
            # platforms = self.lista_piattafforme,
            # ladders = self.lista_scale,
            gravity_constant = 1.5,
        )

        self.p1.set_physics_engine(self.physics_engine)
        self.e1.set_physics_engine(self.physics_engine)
        

        self.physics_engine.enable_multi_jump(1)
        

        self.background = arcade.load_texture("./assets/sfondoG3.png")

        self.camera.position = (self.p1.center_x, self.p1.center_y)

    def on_draw(self):

        self.clear()

        self.camera.use()
        arcade.draw_texture_rect(
            self.background,
            arcade.LBWH(
                self.camera.position[0], 
                self.camera.position[1], 
                self.SCREEN_WIDTH, 
                self.SCREEN_HEIGHT)
            )
        
        self.scene.draw()
        
        self.camera_ui.use()
        
        #self.draw_health_bar()

    def on_update(self, delta_time):

        self.scene.update(delta_time)
        self.scene.update_animation(delta_time)
        self.physics_engine.update()

        self.aggiorna_camera()

        self.p1.update_jump_reset()
        
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

    def on_key_release(self, tasto, modificatori):

        if tasto == arcade.key.SPACE:
            pass
        elif tasto in (arcade.key.A, arcade.key.D, arcade.key.RIGHT, arcade.key.LEFT):
            self.p1.stop()
        elif tasto == arcade.key.ESCAPE:
            self.setup()

def main():
    window = GameView(
        GameView.SCREEN_WIDTH,
        GameView.SCREEN_HEIGHT,
        "Il mio giochino"
    )
    #window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
