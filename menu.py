import arcade
import arcade.gui

class MenuView(arcade.View):

    SCREEN_WIDTH = 960
    SCREEN_HEIGHT = 540

    def __init__(self):
        super().__init__()

        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        play_button = arcade.gui.UIFlatButton(text="Avvio", width = 150)
        quit_button = arcade.gui.UIFlatButton(text="Esci", width = 150)

        play_button.on_click = self.play
        quit_button.on_click = self.exit
        layout = arcade.gui.UIBoxLayout(spacing = 50)
        layout.add(play_button)
        layout.add(quit_button)
        self.manager.add(arcade.gui.UIAnchorLayout(children=[layout]))

        self.background = arcade.load_texture("./assets/sfondo-menu2.png")

    def on_draw(self):
        
        self.clear()
        self.window.default_camera.use()
        arcade.draw_texture_rect(self.background,
                                 arcade.LBWH(0,0,self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.manager.draw()

    def play(self, event):
        from crediti import CreditiView
        crediti_view = CreditiView()
        crediti_view.window = self.window
        self.window.show_view(crediti_view)
        
    def exit(self, event):
        arcade.exit()
        
    def on_hide_view(self):
        self.manager.disable()