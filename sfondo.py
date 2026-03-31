import arcade
import arcade.future.background as background
from player import Player


WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 800
CAMERA_SPEED = 0.1


class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.background_color = (162, 84, 162, 255)
        self.camera = arcade.Camera2D()

        # Creiamo il gruppo che gestirà tutti i layer
        self.backgrounds = background.ParallaxGroup()

        bg_size = (WINDOW_WIDTH, WINDOW_HEIGHT)

        # Aggiungiamo i layer dal più lontano al più vicino.
        # depth alto = lontano = scorre lento
        self.backgrounds.add_from_file("assets/Wood/Background layers/sfondo.png",    size=bg_size, depth=11.0)
        self.backgrounds.add_from_file("assets/Wood/Background layers/sfondo1.png", size=bg_size, depth=10.0)
        self.backgrounds.add_from_file("assets/Wood/Background layers/sfondo2.png",   size=bg_size, depth=9.0)
        self.backgrounds.add_from_file("assets/Wood/Background layers/sfondo3.png",   size=bg_size, depth=8.0)
        self.backgrounds.add_from_file("assets/Wood/Background layers/sfondo4.png",   size=bg_size, depth=7.0)
        self.backgrounds.add_from_file("assets/Wood/Background layers/sfondo5.png",   size=bg_size, depth=6.0)
        self.backgrounds.add_from_file("assets/Wood/Background layers/sfondo6.png",   size=bg_size, depth=5.0)
        self.backgrounds.add_from_file("assets/Wood/Background layers/sfondo7.png",   size=bg_size, depth=4.0)
        self.backgrounds.add_from_file("assets/Wood/Background layers/sfondo8.png",   size=bg_size, depth=3.0)
        self.backgrounds.add_from_file("assets/Wood/Background layers/sfondo9.png",   size=bg_size, depth=2.0)
        self.backgrounds.add_from_file("assets/Wood/Background layers/sfondo10.png",   size=bg_size, depth=1.0)
        self.backgrounds.add_from_file("assets/Wood/Background layers/sfondo11.png",   size=bg_size, depth=0.5)       

        self.player = Player(self.scene)
        self.player.bottom = 0 # mette il giocatore in basso
        self.x_velocity = 0 # usata per la gestione del movimento, per spostare il giocatore

    def on_draw(self):

        self.clear() # pulisco lo schermo
        self.camera.use()

        bg = self.backgrounds

        # Sposta i layer simulando la profondità
        bg.offset = self.camera.bottom_left
        # Segue la camera per simulare un "mondo infinito"
        bg.pos = self.camera.bottom_left

        bg.draw()

        arcade.draw_sprite(self.player)

    def pan_camera_to_player(self):

        # La camera segue il giocatore in modo "smooth" (lerp). Guarda l'altro blog sulla camera
        self.camera.position = arcade.math.lerp_2d(
            self.camera.position,
            (self.player.center_x, self.height // 2),
            CAMERA_SPEED
        )

    def on_update(self, delta_time: float):

        self.player.center_x += self.x_velocity * delta_time
        self.pan_camera_to_player()
