import pygame
from vue.abstract import Abstract
import keyboard

class PygameDisplay(Abstract):
    
    def __init__(self, jeu) -> None:
        pygame.init()
        self.width = jeu.largeur
        self.height = jeu.longueur
        self.cell_size = 10
        self.screen = pygame.display.set_mode((self.width * self.cell_size, self.height * self.cell_size))
        self.screen.fill((255, 255, 255))
        pygame.display.flip()

    def afficher_etat(self, jeu):
        self.screen.fill((255, 255, 255))
        for x in range(self.width):
            for y in range(self.height):
                if jeu.get_case(x, y):
                    pygame.draw.rect(self.screen, (0, 0, 0), (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))
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