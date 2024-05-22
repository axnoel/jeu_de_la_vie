# Importer le fichier de vue
from vue.textuel import VueTextuelle
from vue.pygame import PygameDisplay
import time


# Importer le fichier de modèle
from modele.grille import Grille

jeu = Grille(80, 80)


vue = PygameDisplay(jeu)


# Définir le nombre de FPS souhaité
fps = 20
frame_duration = 1 / fps

while(True):
    start_time = time.time()
    vue.afficher_etat(jeu)
    vue.obtenir_input(jeu)
    jeu.next_round()
    elapsed_time = time.time() - start_time
    time_to_sleep = frame_duration - elapsed_time
    if time_to_sleep > 0:
        time.sleep(time_to_sleep)