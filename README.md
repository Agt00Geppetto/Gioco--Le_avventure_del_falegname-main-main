## Le Avventure del Falegname

Un gioco platform 2D sviluppato in Python con la libreria **Arcade**, in cui vestirai i panni di un avventuriero in cerca di redenzione.

---

## Trama

Un avventuriero cacciatosi nei guai nel suo regno è stato mandato in esilio. Per tornare a casa dovrai sconfiggere tutti i nemici sul tuo cammino.

---

## Requisiti

- Python 3.9 o superiore
- Libreria [Arcade](https://api.arcade.academy/)

Installa le dipendenze con:

```bash
pip install arcade
```

---

## Come Avviare il Gioco

1. Clona la repository:

```bash
git clone https://github.com/Agt00Geppetto/Gioco--Le_avventure_del_falegname-main-main.git
```

2. Avvia il gioco:

```bash
python avvio.py
```

---

## Comandi

| Tasto | Azione |
|---|---|
| `←` o `A` / `→` o `D` | Muoviti a sinistra / destra |
| `SHIFT` + `←` o `A` / `→` o `D` | Corri a sinistra / destra |
| `SPAZIO` | Salta (doppio salto disponibile) |
| `E` | Attacca i nemici |
| `INVIO` | Conferma / Avvia il gioco dalla schermata comandi |
| `ESC` | Pausa |

---

## Meccaniche di Gioco

**Vita** — Il personaggio ha 100 punti vita. Se la vita scende a zero, la partita è persa.

**Stamina** — Il personaggio ha 50 punti stamina. Correre e attaccare consumano stamina, che si rigenera automaticamente quando si è fermi. (Ancora in fase di sviluppo, per ora non funziona)

**Doppio Salto** — Il giocatore può effettuare fino a 2 salti consecutivi prima di toccare terra.

**Attacco** — Il raggio d'attacco è di 100 pixel. Ogni colpo infligge 10 punti danno ai nemici.

**Pozioni & Monete** — Durante il livello troverai pozioni curative e monete da raccogliere.

---

## Struttura del Progetto

```
├── avvio.py          # Punto di ingresso del gioco
├── game_project.py   # Logica principale del gioco
    ├── player.py         # Gestione del personaggio giocante
    ├── nemici.py         # Comportamento dei nemici
        ├── animazione.py     # Sistema di animazioni
        ├── barra.py          # Barre vita e stamina
    ├── menu.py           # Schermata del menu principale
    ├── comandi.py        # Schermata dei comandi
    ├── pausa.py          # Schermata di pausa
    ├── inventario.py     # Sistema inventario
    ├── pozioni.py        # Gestione pozioni
    ├── monete.py         # Gestione monete
    ├── muri.py           # Collisioni con i muri
        ├── oggetti.py        # Classe per distinguere oggetti rompibili dai muri
    ├── piattaforme.py    # Gestione piattaforme
    ├── sfondo.py         # Gestione dello sfondo
    ├── vittoria.py       # Schermata di vittoria
    ├── sconfitta.py      # Schermata di sconfitta
    ├── crediti.py        # Schermata crediti
    └── assets/           # Risorse grafiche e audio
```

---

## 👤 Autore

**Agt00Geppetto** — [GitHub](https://github.com/Agt00Geppetto)

---

## Possibili aggiornamenti

1. Ottimizzazione della stamina