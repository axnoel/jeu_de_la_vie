import abc
class Abstract (abc.ABC):

    def __init__(self, jeu) -> None:
        pass

    @abc.abstractmethod
    def afficher_etat(self, jeu):
        pass

    @abc.abstractmethod
    def obtenir_input(self, jeu):
        pass