import arcade

class GameOverView(arcade.View):

    SCREEN_WIDTH = 960
    SCREEN_HEIGHT = 540

    def __init__(self, punteggio: int):
        super().__init__()

        self.punteggio = punteggio
        self.background = arcade.load_texture("./assets/sconfitta-view.png")

    def on_draw(self):

        self.clear()
        arcade.draw_texture_rect(self.background,
                                 arcade.LBWH(0,0,self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        arcade.draw_text(f"Punteggio: {self.punteggio}", 480, 280,
                         arcade.color.WHITE, font_size=28, anchor_x="center")
        arcade.draw_text("Rigioca -> INVIO   Menu -> M", 480, 180,
                         arcade.color.LIGHT_GRAY, font_size=18, anchor_x="center")

    def on_key_press(self, key, modifiers):
        if key == arcade.key.RETURN:
            from game_project import Gioco
            nuova_partita = Gioco()
            nuova_partita.setup()
            self.window.show_view(nuova_partita)
        elif key == arcade.key.M:
            from menu import MenuView
            self.window.show_view(MenuView())