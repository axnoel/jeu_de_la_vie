from vue.abstract import Abstract


class VueTextuelle(Abstract):

    def __init__(self, jeu) -> None:
        pass

    def afficher_etat(self, jeu):
        print(jeu)
    
    def obtenir_input(self, jeu):
        return input("Appuyez sur une touche pour passer à l'état suivant : ")