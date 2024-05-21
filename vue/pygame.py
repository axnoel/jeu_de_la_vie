import pygame
from vue.abstract import Abstract
import keyboard

class PygameDisplay(Abstract):
    
    def __init__(self, jeu) -> None:
        pygame.init()
        self.width = jeu.largeur
        self.height = jeu.longueur
        self.cell_size = 10
        self.screen = pygame.display.set_mode((self.width * self.cell_size + 250, self.height * self.cell_size))
        self.base_affichage()
        pygame.display.flip()

    def afficher_etat(self, jeu):
        

        for x in range(self.width):
            for y in range(self.height):
                if jeu.get_case(x, y):

                    pygame.draw.rect(self.screen, (200, 200, 200), (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))
                    pygame.draw.rect(self.screen, (0, 0, 0), (x * self.cell_size +1, y * self.cell_size +1, self.cell_size -2 , self.cell_size -2))
        pygame.display.flip()
    
    def obtenir_input(self):
        paused = True
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            if keyboard.is_pressed('enter'):
                paused = False


    def base_affichage(self):
        self.screen.fill((255, 255, 255))
        pygame.draw.rect(self.screen, (200, 200, 200), (self.width * self.cell_size, 0, 250, self.height * self.cell_size))
        pygame.draw.rect(self.screen, (0, 0, 0), (self.width * self.cell_size, 0, 1, self.height * self.cell_size))
