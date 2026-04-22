import arcade
from comandi import ComandiView

class CreditiView(arcade.View):

    SCREEN_WIDTH = 960
    SCREEN_HEIGHT = 650

    def __init__(self):
        super().__init__()

        self.background = arcade.load_texture("./assets/Geppetto's industries.png")

    def on_draw(self):
        
        self.clear()
        arcade.draw_texture_rect(self.background,
                                 arcade.LBWH(0,-50,self.SCREEN_WIDTH, self.SCREEN_HEIGHT))  
        
    def on_key_press(self, tasto, modifiers):

        if tasto == arcade.key.RETURN:
            comandi_view = ComandiView()
            self.window.show_view(comandi_view)