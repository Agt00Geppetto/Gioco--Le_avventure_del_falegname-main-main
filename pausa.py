import arcade
import arcade.gui

class PauseView(arcade.View):

    SCREEN_WIDTH = 960
    SCREEN_HEIGHT = 540

    def __init__(self, game_view):
        super().__init__()
        
        self.game_view = game_view  # teniamo il riferimento alla partita in corso
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        resume_bottom = arcade.gui.UIFlatButton(text="Riprendi", width = 150)
        reset_bottom = arcade.gui.UIFlatButton(text="Riavvia", width = 150)
        menu_bottom = arcade.gui.UIFlatButton(text="Menu", width = 150)
        quit_bottom = arcade.gui.UIFlatButton(text="Esci", width = 150)

        resume_bottom.on_click = self.resume
        reset_bottom.on_click = self.reset
        quit_bottom.on_click = self.quit
        menu_bottom.on_click = self.menu

        layout = arcade.gui.UIBoxLayout(spacing = 50)
        layout.add(resume_bottom)
        layout.add(reset_bottom)
        layout.add(quit_bottom)
        layout.add(menu_bottom)

        self.manager.add(arcade.gui.UIAnchorLayout(children=[layout]))

    def on_draw(self):

        self.game_view.on_draw()  # Disegniamo il gioco sottostante. Non chiamando mai on_update, il gioco viene "freezato"

        arcade.draw_rect_filled(
            arcade.XYWH(480, 270, 960, 540),
            (0, 0, 0, 150)  # nero semitrasparente
        )
        arcade.draw_text("PAUSA", 480, 400,
                         arcade.color.BLEU_DE_FRANCE, font_size=48, font_name = ("./assets/d_i_y_75/D.I.Y.'75.ttf"), anchor_x="center")
        self.manager.draw()
    
    def resume(self,event):
        self.window.show_view(self.game_view)

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
        self.game_view.camera.position = (self.SCREEN_WIDTH/2, self.SCREEN_HEIGHT/2)
        menu_view = MenuView()
        self.window.show_view(menu_view)

    def quit(self, event):
        arcade.exit()