import arcade
from menu import MenuView

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(960, 540, "Le avventure del falegname")
        menu = MenuView()
        self.show_view(menu)  # la prima view da mostrare


def main():
    window = MyGame()
    arcade.run()

main()