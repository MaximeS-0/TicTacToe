import pygame
from UI.background.bouncingBackground import BouncingBackground
from UI.screen.screen import Screen
from UI.button import Button

class Main_screen(Screen):

    def __init__(self, screen):
        super().__init__(screen)

        #load background
        self.background = BouncingBackground("./rsc/background/main_background.png", 200, self.screen.get_height())

        #load button
        self.button_Play = Button(225,80, "./rsc/button/main_screen/Bouton_Play.png", 1)
        self.button_Score = Button(225,210, "./rsc/button/main_screen/Bouton_Score.png", 1)
        self.button_Options = Button(225,340, "./rsc/button/main_screen/Bouton_Options.png", 1)
        self.button_Exit = Button(225,470, "./rsc/button/main_screen/Bouton_Exit.png", 1)


    def specificScreenDisplay(self):

        self.background.show(self.screen)

        if self.button_Play.draw(self.screen):
               print("Button Play")

        if self.button_Score.draw(self.screen):
               print("Button score")

        if self.button_Options.draw(self.screen):
               print("Button options")

        if self.button_Exit.draw(self.screen):
               print("Button Exit")
               self.running = False
