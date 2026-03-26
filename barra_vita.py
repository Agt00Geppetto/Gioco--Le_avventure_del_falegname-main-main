import random
import arcade

class Barra:

    WIDTH_BARRA = 100
    HEIGHT_BARRA = 40

    def __init__(self):
        super().__init__()
        
        self.max_vita: float = 100.0
        self.vita_corrente: float = 100.0
        percentuale = None

    def draw_barra(self):

        #quadrato di sfondo per la vita
        arcade.draw_rect_filled(
            self.max_vita,
            arcade.XYWH(100, 500, self.WIDTH_BARRA, self.HEIGHT_BARRA),
            (0, 0, 0, 150)
        )

        #quadrato della vita
        arcade.draw_rect_filled(
            self.vita_corrente,
            arcade.XYWH(100, 500, self.WIDTH_BARRA, self.HEIGHT_BARRA),
            arcade.color.GREEN
        )

    def update(self):
        pass

    def morte(self):
        pass

    def cura(self):
        pass

    def danno(self):
        pass

