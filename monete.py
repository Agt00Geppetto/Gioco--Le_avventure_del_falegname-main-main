import arcade 
import random

class Monete:
    
    def __init__(self,scene):

        self.scene = scene
        self.m = 'C:\\Users\\gabry\\Desktop\\Gioco--Le_avventure_del_falegname-main-main\\assets\\moneta.png'
        self.valore_m = 10
        self.m_c = 'C:\\Users\\gabry\\Desktop\\Gioco--Le_avventure_del_falegname-main-main\\assets\\moneta-corrotta.png'
        self.valore_mc = 15
        self.l = 'C:\\Users\\gabry\\Desktop\\Gioco--Le_avventure_del_falegname-main-main\\assets\\lingotto.png'
        self.valore_l = 30
        self.l_c = 'C:\\Users\\gabry\\Desktop\\Gioco--Le_avventure_del_falegname-main-main\\assets\\lingotto-corrotto.png'
        self.valore_l_c = 40
        self.genera_gioielli()
        
    def genera_gioielli(self):

        for x in range(200, 2900, 100):
            gioielli = ["monete", "lingotti"]
            probabilità = [75, 25]
            gioiello_estratto = random.choices(gioielli, weights = probabilità, k = 1)[0]

            # Monete estraibili
            if gioiello_estratto == "monete":
                opzioni =  [self.m, self.m_c]
                pesi = [70, 30]
            # Lingotti estraibili
            elif gioiello_estratto == "lingotti":
                opzioni = [self.l, self.l_c]
                pesi = [80, 20]

            risultato = random.choices(opzioni, weights = pesi, k=1)[0]

            gioiello = arcade.Sprite(risultato)
            gioiello.center_x = random.randint(200,2900)
            gioiello.center_y = random.randint(100,300)
            gioiello.scale = 0.05
            self.scene.add_sprite("Coins", gioiello)