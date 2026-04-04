import random
import arcade

class BarraProgressiva():

    WIDTH_BARRA = 100
    HEIGHT_BARRA = 20
    OFFSET_Y = 50

    def __init__(self, valore_corrente, max_valore, entità = arcade.Sprite):
        
        self.max_valore: float = max_valore
        self.valore_corrente: float = valore_corrente 
        self.entità = entità  

    def draw_barra(self):

        percentuale = self.valore_corrente/self.max_valore
        larghezza_visiva = self.WIDTH_BARRA * percentuale

        left = self.entità.center_x - self.WIDTH_BARRA
        bottom = self.entità.center_y + self.OFFSET_Y 

        # quadrato di sfondo della vita
        arcade.draw_rect_filled(
            arcade.LBWH(
                left,
                bottom,
                self.WIDTH_BARRA,
                self.HEIGHT_BARRA
            ),
            (0, 0, 0, 150)
        )

        # quadrato della vita
        arcade.draw_rect_filled(
            arcade.LBWH(
                left,
                bottom,
                larghezza_visiva,
                self.HEIGHT_BARRA
            ),
            arcade.color.GREEN
        )