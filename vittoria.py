import arcade
import arcade.gui

class WinView(arcade.View):

    SCREEN_WIDTH = 960
    SCREEN_HEIGHT = 540

    def __init__(self):
        super().__init__()

        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        menu_button = arcade.gui.UIFlatButton(text="Menu", width = 150)
        quit_button = arcade.gui.UIFlatButton(text="Esci", width = 150)

        menu_button.on_click = self.menu
        quit_button.on_click = self.exit
        layout = arcade.gui.UIBoxLayout(spacing = 50)
        layout.add(menu_button)
        layout.add(quit_button)
        self.manager.add(arcade.gui.UIAnchorLayout(children=[layout]))

        self.background = arcade.load_texture("./assets/vittoria-view.png")

    def on_draw(self):
        
        self.clear()
        arcade.draw_texture_rect(self.background,
                                 arcade.LBWH(0,0,self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.manager.draw()
        
    def exit(self, event):
        arcade.exit()

    def menu(self, event):
        from menu import MenuView
        self.manager.disable()
        menu_view = MenuView()
        self.window.show_view(menu_view)