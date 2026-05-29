import arcade

class Musica():

    def __init__(self):
        
        self.gioco = arcade.load_sound("./assets/suoni/musica_gioco.mp3")
        self.collezionabili = arcade.load_sound("./assets/suoni/colleziona.mp3")
        self.perso = arcade.load_sound("./assets/suoni/sconfitta.mp3")
        self.colpo = arcade.load_sound("./assets/suoni/colpo.mp3")
        self.fine = arcade.load_sound("./assets/suoni/livello_superato.mp3")
        self.volume = True