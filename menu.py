import arcade
from game_project import GameView

class MenuView(arcade.View):
    def __init__(self):
        super().__init__()

    def on_draw(self):
        self.clear()
        arcade.draw_text("IL MIO GIOCO", 480, 350,
                         arcade.color.WHITE, font_size=48, anchor_x="center")
        arcade.draw_text("Premi INVIO per iniziare", 480, 250,
                         arcade.color.LIGHT_GRAY, font_size=20, anchor_x="center")
        

    def on_key_press(self, tasto, modifiers):
        if tasto == arcade.key.RETURN:
            game_view = GameView()
            game_view.setup()
            self.window.show_view(game_view)
