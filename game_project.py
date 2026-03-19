import arcade
import os
import random
#from inventario import Inventario
from player import Player
from muri import Muri
from nemici import Enemy
#from barra_vita import Barra

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

    def on_show_view(self):
        """Viene chiamato quando la view diventa attiva"""
        self.setup()

    def setup(self):
        self.scene = arcade.Scene()

        self.camera = arcade.Camera2D()
        self.camera_ui = arcade.Camera2D()

        self.p1 = Player(self.scene)

        self.e1 = Enemy("./assets/Legnamorta.png", 0.8)
        self.e1.center_x = 800
        self.e1.center_y = 350
        self.scene.add_sprite("Enemy", self.e1)

        self.muri = Muri(self.scene)

        self.physics_engine = arcade.PhysicsEnginePlatformer(
            player_sprite=self.p1,
            walls=self.scene["Walls"],
            gravity_constant=1.5,
        )

        self.p1.set_physics_engine(self.physics_engine)
        self.scene = Player(self.p1.set_physics_engine)
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


        self.camera.use()
        self.scene.draw()


    def on_update(self, delta_time):
        self.scene.update(delta_time)
        self.scene.update_animation(delta_time)
        self.physics_engine.update()

        self.aggiorna_camera()
        Player(self.p1.update_jump_reset())
 
    def aggiorna_camera( self):
        cam_x, cam_y = self.camera.position

        target_x = cam_x + (self.p1.center_x - cam_x) * 0.99
        target_y = cam_y + (self.p1.center_y - cam_y) * 0.99

        target_x = max(self.SCREEN_WIDTH / 2, min(target_x, self.WORLD_WIDTH - self.SCREEN_WIDTH / 2))
        target_y = max(self.SCREEN_HEIGHT / 2, min(target_y, self.WORLD_HEIGHT - self.SCREEN_HEIGHT / 2))

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

    def on_key_release(self, tasto, modificatori):
        if tasto in (arcade.key.A, arcade.key.D, arcade.key.RIGHT, arcade.key.LEFT):
            self.p1.stop()
        elif tasto == arcade.key.ESCAPE:
            self.setup()
def main():
    window = arcade.Window(960, 540, "Il mio giochino", fullscreen=False)

    game_view = GameView()
    window.show_view(game_view)

    arcade.run()

if __name__ == "__main__":
    main()
