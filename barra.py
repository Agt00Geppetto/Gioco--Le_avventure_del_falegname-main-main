import random
import arcade

class BarraProgressiva():

    WIDTH_BARRA = 100
    HEIGHT_BARRA = 20

    def __init__(self):
        super().__init__()
        
        self.max_valore: float = 100.0
        self.valore_corrente: float = 100.0   

    def draw_barra(self):

        percentuale = self.valore_corrente/self.max_valore
        larghezza_visiva = self.WIDTH_BARRA * percentuale 

        # quadrato di sfondo della vita
        arcade.draw_rect_filled(
            arcade.LBWH(
                50,
                500,
                self.WIDTH_BARRA,
                self.HEIGHT_BARRA
            ),
            (0, 0, 0, 150)
        )

        # quadrato della vita
        arcade.draw_rect_filled(
            arcade.LBWH(
                50,
                500,
                larghezza_visiva,
                self.HEIGHT_BARRA
            ),
            arcade.color.GREEN
        )
    

