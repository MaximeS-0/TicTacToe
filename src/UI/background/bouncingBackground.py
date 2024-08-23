import pygame
import random
from UI.background.background import Background

class BouncingBackground(Background):
    
    def __init__(self, imageFile, bouncingSpeed, screenDimension):
        super().__init__(imageFile, screenDimension)

        self.coord = [random.randint(-(self.img.get_width()-self.screenDimension), 0),  #x
                      random.randint(-(self.img.get_height()-self.screenDimension), 0)] #y
        

        self.boucingSpeed_x = random.uniform(-bouncingSpeed, bouncingSpeed)
        self.boucingSpeed_y = random.uniform(-bouncingSpeed, bouncingSpeed)

        self.clock = pygame.time.Clock()
        self.frameRate = 60


    def show(self, surface):
        self.UpdateCoords() #Move the background
        super().show(surface) #Show the background

    def UpdateCoords(self):
        time = self.clock.tick(self.frameRate)/1000.0

        distance_y = self.boucingSpeed_y * time
        distance_x = self.boucingSpeed_x * time

        self.coord[0] += distance_x
        self.coord[1] += distance_y

        changeOfSpeed = random.uniform(0.8, 1.2)

        if self.coord[0] >= 0:
            self.coord[0] = 0
            self.boucingSpeed_x = self.boucingSpeed_x * -changeOfSpeed

        if self.coord[0] <= -(self.img.get_width()-self.screenDimension):
            self.coord[0] = -(self.img.get_width()-self.screenDimension)
            self.boucingSpeed_x = self.boucingSpeed_x *-changeOfSpeed

        if self.coord[1] >= 0:
            self.coord[1] = 0
            self.boucingSpeed_y = self.boucingSpeed_y *-changeOfSpeed

        if self.coord[1] <= -(self.img.get_height()-self.screenDimension):
            self.coord[1] = -(self.img.get_height()-self.screenDimension)
            self.boucingSpeed_y = self.boucingSpeed_y *-changeOfSpeed