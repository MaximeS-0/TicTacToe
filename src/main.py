import pygame

from UI.background.bouncingBackground import BouncingBackground
from UI.screen.main_screen import Main_screen
from UI.button import Button

screen_dimension = 600


pygame.init()
pygame.mouse.set_visible(True)
pygame.display.set_caption('Tic Tac Toe')

screen = pygame.display.set_mode((screen_dimension,screen_dimension))

mainScreen = Main_screen(screen)
mainScreen.showScreen()
