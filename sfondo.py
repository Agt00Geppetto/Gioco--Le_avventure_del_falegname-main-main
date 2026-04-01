import arcade
import arcade.future.background as background

WINDOW_WIDTH = 960
WINDOW_HEIGHT = 540


class ParallaxBackground:
    def __init__(self):

        self.backgrounds = background.ParallaxGroup()

        bg_size = (WINDOW_WIDTH, WINDOW_HEIGHT)


        # Aggiungiamo i layer dal più lontano al più vicino.
        # depth alto = lontano = scorre lento
        self.backgrounds.add_from_file("assets/Wood/Background layers/sfondo.png", size=bg_size, depth=11.0)
        self.backgrounds.add_from_file("assets/Wood/Background layers/sfondo1.png", size=bg_size, depth=10.0)
        self.backgrounds.add_from_file("assets/Wood/Background layers/sfondo2.png", size=bg_size, depth=9.0)
        self.backgrounds.add_from_file("assets/Wood/Background layers/sfondo3.png", size=bg_size, depth=8.0)
        self.backgrounds.add_from_file("assets/Wood/Background layers/sfondo4.png", size=bg_size, depth=7.0)
        self.backgrounds.add_from_file("assets/Wood/Background layers/sfondo5.png", size=bg_size, depth=6.0)
        self.backgrounds.add_from_file("assets/Wood/Background layers/sfondo6.png", size=bg_size, depth=5.0)
        self.backgrounds.add_from_file("assets/Wood/Background layers/sfondo7.png", size=bg_size, depth=4.0)
        self.backgrounds.add_from_file("assets/Wood/Background layers/sfondo8.png", size=bg_size, depth=3.0)
        self.backgrounds.add_from_file("assets/Wood/Background layers/sfondo9.png", size=bg_size, depth=2.0)
        self.backgrounds.add_from_file("assets/Wood/Background layers/sfondo11.png", size=bg_size, depth=0.5)

    def draw(self, camera):

        bg = self.backgrounds

        bg.offset = camera.bottom_left
        bg.pos = camera.bottom_left

        bg.draw()