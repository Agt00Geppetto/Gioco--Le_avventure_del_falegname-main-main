import arcade

class SpriteAnimato(arcade.Sprite):
    def __init__(self, scala: float = 1.0):
        super().__init__(scale=scala)
        self.animazioni = {} 
        self.animazione_corrente = None  # Nome dell'animazione attualmente attiva
        self.animazione_default = None  # Nome dell'animazione di default
        self.tempo_frame = 0.0  # Tempo accumulato per il frame corrente
        self.indice_frame = 0  # Indice del frame corrente nell'animazione

    def aggiungi_animazione(
        self,
        nome: str,  # Nome dell'animazione
        percorso: str,  # Percorso dello spritesheet
        frame_width: int,  # Larghezza di ogni frame
        frame_height: int,  # Altezza di ogni frame
        num_frame: int,  # Numero di frame da usare
        colonne: int,  # Numero di colonne nello spritesheet
        durata: float,  # Durata totale dell'animazione
        loop: bool = True,  # Se l'animazione deve ripetersi
        default: bool = False,  # Se è l'animazione di default
        riga: int = 0,  # Riga dello spritesheet da cui partire
    ):
        """
        Carica uno spritesheet e registra l'animazione con il nome dato.

        loop    : se True l'animazione riparte dall'inizio quando finisce
        default : se True questa è l'animazione di riposo (quella a cui si
                  torna automaticamente quando una animazione non in loop finisce)
        riga    : riga dello spritesheet da cui estrarre i frame (0 = prima riga)
        """
        sheet = arcade.load_spritesheet(percorso)  # Carica lo spritesheet dal file
        offset = riga * colonne  # Calcola l'indice di partenza basato sulla riga
        tutti = sheet.get_texture_grid(  # Estrae una griglia di texture dallo spritesheet
            size=(frame_width, frame_height),  # Dimensione di ogni frame
            columns=colonne,  # Numero di colonne
            count=offset + num_frame,  # Numero totale di frame da caricare
        )
        self._registra(nome, tutti[offset:], durata, loop, default)  # Registra l'animazione

    def _registra(self, nome, textures, durata, loop, default=False):  # Metodo interno per registrare animazioni
        """Usato internamente per registrare texture già caricate."""
        self.animazioni[nome] = {  # Inserisce l'animazione nel dizionario
            "textures": textures,  # Lista delle texture (frame)
            "durata_frame": durata / len(textures),  # Tempo per ogni frame
            "loop": loop,  # Se deve ripetersi
        }
        if default or self.animazione_default is None:  # Se è default o non esiste ancora
            self.animazione_default = nome  # Imposta questa animazione come default
        if self.animazione_corrente is None:  # Se non c'è animazione corrente
            self._vai(nome)  # Imposta questa come animazione attiva

    def imposta_animazione(self, nome: str):  # Metodo per cambiare animazione
        """Cambia animazione (ignorata se è già quella attiva, evita reset del frame)."""
        if nome != self.animazione_corrente:  # Controlla se è diversa da quella corrente
            self._vai(nome)  # Cambia animazione

    def _vai(self, nome: str):  # Metodo interno per passare a una nuova animazione
        self.animazione_corrente = nome  # Imposta l'animazione corrente
        self.indice_frame = 0  # Riparte dal primo frame
        self.tempo_frame = 0.0  # Azzera il tempo accumulato
        self.texture = self.animazioni[nome]["textures"][0]  # Imposta la prima texture

    def update_animation(self, delta_time: float = 1 / 60):  # Aggiorna l'animazione nel tempo
        anim = self.animazioni[self.animazione_corrente]  # Ottiene i dati dell'animazione corrente
        self.tempo_frame += delta_time  # Aggiunge il tempo passato

        if self.tempo_frame < anim["durata_frame"]:  # Se non è ancora tempo di cambiare frame
            return  # Esce senza fare nulla

        self.tempo_frame -= anim["durata_frame"]  # Riduce il tempo accumulato
        prossimo = self.indice_frame + 1  # Calcola il prossimo frame

        if prossimo < len(anim["textures"]):  # Se esiste un frame successivo
            self.indice_frame = prossimo  # Passa al frame successivo
        elif anim["loop"]:  # Se siamo alla fine ma l'animazione è in loop
            self.indice_frame = 0  # Torna al primo frame
        else:  # Se l'animazione è finita e non è in loop
            self._vai(self.animazione_default)  # Torna all'animazione di default
            return  # Esce dal metodo

        self.texture = anim["textures"][self.indice_frame]  # Aggiorna la texture visualizzata