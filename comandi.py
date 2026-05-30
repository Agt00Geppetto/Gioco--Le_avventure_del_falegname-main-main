import arcade
from game_project import Gioco

class ComandiView(arcade.View):

    SCREEN_WIDTH = 960
    SCREEN_HEIGHT = 550

    def __init__(self):
        super().__init__()

        self.background = arcade.load_texture("./assets/Comandi.png")

    def on_draw(self):
        
        self.clear()
        arcade.draw_texture_rect(self.background,
                                 arcade.LBWH(0,0,self.SCREEN_WIDTH, self.SCREEN_HEIGHT))  
        
    def on_key_press(self, tasto, modifiers):

        from musica import Musica #sposta la musica da qui, non va bene
        self.suono = Musica()

        if tasto == arcade.key.RETURN:
            game_view = Gioco()
            game_view.setup()
            self.window.show_view(game_view)
            arcade.play_sound(self.suono.gioco, volume = 0.5, loop = True)
