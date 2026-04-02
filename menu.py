import arcade
from game_project import Gioco

class MenuView(arcade.View):

    SCREEN_WIDTH = 960
    SCREEN_HEIGHT = 540

    def __init__(self):
        super().__init__()

        self.background = arcade.load_texture("./assets/sfondo-menu2.png")

    def on_draw(self):
        
        self.clear()
        arcade.draw_texture_rect(self.background,
                                 arcade.LBWH(0,0,self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        arcade.draw_text("INVIO -> Enter", 480, 250,
                         arcade.color.BLEU_DE_FRANCE, font_size=20, anchor_x="center")
        arcade.draw_text("ESCI -> Q", 480, 200,
                         arcade.color.BLEU_DE_FRANCE, font_size=20, anchor_x="center")
        
    def exit(self):
        arcade.exit()
        
    def on_key_press(self, tasto, modifiers):

        if tasto == arcade.key.RETURN:
            game_view = Gioco()
            game_view.setup()
            self.window.show_view(game_view)
        elif tasto == arcade.key.Q:
            self.exit()