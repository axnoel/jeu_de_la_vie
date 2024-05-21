import pygame
from vue.abstract import Abstract

class PygameDisplay(Abstract):
    
    def __init__(self, jeu) -> None:
        pygame.init()
        self.width = jeu.largeur
        self.height = jeu.longueur
        self.cell_size = 10
        self.width_control = 350
        self.screen = pygame.display.set_mode((self.width * self.cell_size + self.width_control, self.height * self.cell_size))
        self.base_affichage()
        


        # Bonton play/pause
        self.play = False

        pygame.display.flip()

    def afficher_etat(self, jeu):
        self.base_affichage()

        for x in range(self.width):
            for y in range(self.height):
                if jeu.get_case(x, y):
                    pygame.draw.rect(self.screen, (200, 200, 200), (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))
                    pygame.draw.rect(self.screen, (0, 0, 0), (x * self.cell_size +1, y * self.cell_size +1, self.cell_size -2 , self.cell_size -2))
        pygame.display.flip()
        return jeu
    
    def obtenir_input(self, jeu):
        paused = True
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                        
                elif event.type == pygame.MOUSEBUTTONDOWN:  # Détecter un clic de souris
                    if event.button == 1: 
                        pos_x, pos_y = event.pos
                        case_x = pos_x // self.cell_size
                        case_y = pos_y // self.cell_size
                        if case_x < self.width and case_y < self.height:
                            jeu.set_case(case_x, case_y, True)
                            self.afficher_etat(jeu)
            # Vérifier si la touche Entrée est pressée
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]: 
                paused = False
            if self.play:
                paused = False

    def base_affichage(self):
        # Fond blanc
        self.screen.fill((255, 255, 255))
        # Rectangle gris pour les boutons
        pygame.draw.rect(self.screen, (200, 200, 200), (self.width * self.cell_size, 0, self.width_control, self.height * self.cell_size))
        # Trait noir pour séparer le jeu des boutons
        pygame.draw.rect(self.screen, (0, 0, 0), (self.width * self.cell_size, 0, 1, self.height * self.cell_size))
        
        
        # taille du texte
        font = pygame.font.Font(None, 25)
        text_press_enter = font.render("Appuyez sur Entrée pour avancer", True, (0, 0, 0))
        size_x, _ = font.size("Appuyez sur Entrée pour avancer")
        pos_text_press_enter = (self.width * self.cell_size +(self.width_control - size_x)/2, 20)
        self.screen.blit(text_press_enter, pos_text_press_enter)

        # Bouton play/pause
        play_button_text = font.render("Play", True, (0, 0, 0))
        size_x, size_y = font.size("Play")
        pos_play_button_text = (self.width * self.cell_size + (self.width_control - size_x)/2, 150)

        pygame.draw.rect(self.screen, (170, 170, 170), (self.width * self.cell_size  + (self.width_control - size_x)/2 -25 , 140, size_x + 50, size_y + 20))
        self.screen.blit(play_button_text, pos_play_button_text)

