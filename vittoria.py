import arcade


class WinView(arcade.View):

    SCREEN_WIDTH = 960
    SCREEN_HEIGHT = 540

    def __init__(self):
        super().__init__()

        self.background = arcade.load_texture("./assets/vittoria-view.png")

    def on_draw(self):
        
        self.clear()
        arcade.draw_texture_rect(self.background,
                                 arcade.LBWH(0,0,self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        arcade.draw_text("MENU -> Enter", 480, 250,
                         arcade.color.BLEU_DE_FRANCE, font_size=20, anchor_x="center")
        # arcade.draw_text("RIPRENDI -> Delete", 480, 150,
        #                  arcade.color.BLEU_DE_FRANCE, font_size=20, anchor_x="center")
        arcade.draw_text("ESCI -> Q", 480, 200,
                         arcade.color.BLEU_DE_FRANCE, font_size=20, anchor_x="center")
        
    def exit(self):
        arcade.exit()
        
    def on_key_press(self, tasto, modifiers):

        if tasto == arcade.key.RETURN:
            from menu import MenuView
            menuvieww_view = MenuView()
            self.window.show_view(menuvieww_view)
        # elif tasto == arcade.key.BACKSPACE:
        #     from game_project import Gioco
        #     gameview_view = Gioco()
        #     self.window.show_view(gameview_view)
        elif tasto == arcade.key.Q:
            self.exit()