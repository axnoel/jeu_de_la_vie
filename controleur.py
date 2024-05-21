# Importer le fichier de vue
from vue.textuel import VueTextuelle
from vue.pygame import PygameDisplay

# Importer le fichier de modèle
from modele.grille import Grille

jeu = Grille(80, 80)

jeu.set_case(10, 10, True)
jeu.set_case(10, 11, True)
jeu.set_case(10, 12, True)
jeu.set_case(11, 12, True)
jeu.set_case(12, 11, True)

vue = PygameDisplay(jeu)

while(True):
    vue.afficher_etat(jeu)
    vue.obtenir_input()
    jeu.next_round()