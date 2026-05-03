import random
import arcade

class BarraProgressiva():

    WIDTH_BARRA = 100

    def __init__(self, valore_corrente, max_valore):
        
        self.max_valore: float = max_valore
        self.valore_corrente: float = valore_corrente

    def draw_barra(self, left, bottom, color, altezza):

        percentuale = self.valore_corrente/self.max_valore
        larghezza_visiva = self.WIDTH_BARRA * percentuale

        # quadrato di sfondo della vita
        arcade.draw_rect_filled(
            arcade.LBWH(
                left,
                bottom,
                self.WIDTH_BARRA,
                altezza
            ),
            (0, 0, 0, 150)
        )

        # quadrato della vita
        arcade.draw_rect_filled(
            arcade.LBWH(
                left,
                bottom,
                larghezza_visiva,
                altezza
            ),
            color
        )