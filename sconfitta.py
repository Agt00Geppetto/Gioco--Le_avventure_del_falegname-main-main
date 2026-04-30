import arcade
import arcade.gui

class GameOverView(arcade.View):

    SCREEN_WIDTH = 960
    SCREEN_HEIGHT = 540

    def __init__(self, punteggio: int):
        super().__init__()

        self.punteggio = punteggio

        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        reset_bottom = arcade.gui.UIFlatButton(text="Riavvia", width = 150)
        menu_bottom = arcade.gui.UIFlatButton(text="Menu", width = 150, height = 49)
        quit_bottom = arcade.gui.UIFlatButton(text="Esci", width = 150)

        reset_bottom.on_click = self.reset
        quit_bottom.on_click = self.quit
        menu_bottom.on_click = self.menu

        layout = arcade.gui.UIBoxLayout(spacing = 50)
        layout.add(reset_bottom)
        layout.add(quit_bottom)
        layout.add(menu_bottom)
        self.manager.add(arcade.gui.UIAnchorLayout(children=[layout]))

        self.background = arcade.load_texture("./assets/sconfitta-view.png")

    def on_draw(self):

        self.clear()
        arcade.draw_texture_rect(self.background,
                                 arcade.LBWH(0,0,self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        arcade.draw_text(f"Punteggio: {self.punteggio}", 480, 100,
                         arcade.color.BLEU_DE_FRANCE, font_size=28, anchor_x="center")
        self.manager.draw()

    def reset(self, event):
        from game_project import Gioco
        self.gioco = Gioco()
        self.gioco.window = self.window
        self.window.show_view(self.gioco)
        self.gioco.punteggio = 0
        self.gioco.stato = None

    def menu(self, event):
        from menu import MenuView
        self.manager.disable()
        menu_view = MenuView()
        self.window.show_view(menu_view)

    def quit(self, event):
        arcade.exit()