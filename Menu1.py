import pygame
from pygame.locals  import * 
from Button import *
from Game import * 

class Menu:
    """Starting menu for the brick breaker game"""

    def __init__(self, screen, width, height, fps):
        self.screen = screen
        self.width = width
        self.height = height
        self.fps = fps
        self.running = True
        self.clock = pygame.time.Clock()

        # Import des images
        self.background = pygame.image.load("background.png")
        self.title = pygame.image.load("Brick_Breaker_Font.png")
        self.start_img = pygame.image.load("start_button.png")
        self.exit_img = pygame.image.load("quit_button.png")
        self.options_img = pygame.image.load("options_button.png")

        # Mise à l'échelle des images
        self.start_img = pygame.transform.scale(self.start_img, (int(self.width * 0.6), int(self.height * 0.2)))
        self.options_img = pygame.transform.scale(self.options_img, (int(self.width * 0.5), int(self.height * 0.15)))
        self.title = pygame.transform.scale(self.title, (int(self.width * 0.9), int(self.height * 0.3)))
        self.exit_img = pygame.transform.scale(self.exit_img, (int(self.width * 0.4), int(self.height * 0.1)))

        # Creation des boutons
        self.start_button = Button(int(self.width * 0.2), int(self.height * 0.5), self.start_img)
        self.options_button = Button(int(self.width * 0.25), int(self.height * 0.7), self.options_img)
        self.exit_button = Button(int(self.width * 0.3), int(self.height * 0.85), self.exit_img)

    # Méthode permettant de lancer la boucle de jeu 
    def start_game(self):
        game = Game(self.screen, self.width, self.height, self.fps)
        game.run()


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.exit_button.click():
                    self.running = False
                    pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.start_button.click():
                    self.start_game()

    def update(self):
        if self.start_button.drawButton(self.screen):
            self.start_game()

    def display(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.title, (self.width * 0.05, self.height * 0.2))
        self.start_button.drawButton(self.screen)
        self.options_button.drawButton(self.screen)

        
        self.exit_button.drawButton(self.screen) 
            

        pygame.display.flip()
       

       
    def run(self) :
        while self.running : 
            self.handle_events()
            self.update()
            self.display()
            self.clock.tick(self.fps)


        
pygame.init()


menu_fps = 60
menu_width = 500
menu_height = 500
menu_screen = pygame.display.set_mode((menu_width,menu_height))
menu_title = pygame.display.set_caption("Casse Brique")
menu = Menu(menu_screen,menu_width,menu_height,menu_fps)
menu.run()

