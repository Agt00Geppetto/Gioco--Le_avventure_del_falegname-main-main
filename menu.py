import arcade
from game_project import GameView

class MenuView(arcade.View):

    SCREEN_WIDTH = 960
    SCREEN_HEIGHT = 540

    def __init__(self):
        super().__init__()

        self.background = arcade.load_texture("./assets/sfondo_menu.png")

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rect(self.background,
                                 arcade.LBWH(0,0,self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        arcade.draw_text("INVIO", 480, 250,
                         arcade.color.LIGHT_GRAY, font_size=20, anchor_x="center")
        

    def on_key_press(self, tasto, modifiers):
        if tasto == arcade.key.RETURN:
            game_view = GameView()
            game_view.setup()
            self.window.show_view(game_view)
