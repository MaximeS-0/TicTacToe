import pygame

class Screen():
    def __init__(self, screen):
        self.screen = screen
        self.running = True #Is the screen active
        

    def showScreen(self):
        self.running = True

        while self.running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.specificScreenDisplay()

            pygame.display.update()

    def specificScreenDisplay(self):
        pass