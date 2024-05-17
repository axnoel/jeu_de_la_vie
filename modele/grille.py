class Grille:
    def __init__(self, largeur, longueur):
        self.largeur = largeur
        self.longueur = longueur
        self.grille = [[False] * largeur for _ in range(longueur)]

    # Méthodes de la classe Grille

    # Permet de récupérer la valeur d'une case % la longueur et la largeur de la grille
    def get_case(self, x, y):
        return self.grille[y%self.largeur][x%self.longueur]

    # Permet de modifier la valeur d'une case % la longueur et la largeur de la grille
    def set_case(self, x, y, valeur):
        self.grille[y%self.largeur][x%self.longueur] = valeur

    # Permet de récupérer le nombre de voisins vivants d'une case
    def get_nbr_voisins(self, x, y):
        return [self.get_case(x+dx, y+dy) for dx in (-1, 0, 1) for dy in (-1, 0, 1) if dx != 0 or dy != 0].count(True)

    # Permet de passer à la génération suivante
    def next_round(self):
        copie_grille = [[False] * self.largeur for _ in range(self.longueur)]
        for y in range(self.longueur):
            for x in range(self.largeur):
                voisins = self.get_nbr_voisins(x, y)

                # Si une cellule est vivante et a 2 ou 3 voisins, elle reste vivante
                if self.grille[y][x] == True and voisins in (2, 3):
                    copie_grille[y][x] = True
                # Si une cellule est morte et a 3 voisins, elle devient vivante
                elif self.grille[y][x] == False and voisins == 3:
                    copie_grille[y][x] = True
        self.grille = copie_grille

    # Permet d'afficher la grille
    def __str__(self):
        return '\n'.join(''.join('0' if self.grille[y][x] else '  ' for x in range(self.largeur)) for y in range(self.longueur))