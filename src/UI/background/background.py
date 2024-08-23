import pygame

class Background:
    def __init__(self, imageFile, screenDimension):
        self.img = pygame.image.load(imageFile)
        self.screenDimension = screenDimension    

        self.coord = [0,0] #Top left corner of the image

    def show(self, surface):
        #Draw the image. The coordinate is the screen relative to the image.
        #The coordinate (-600, -600) will draw the image starting from the pixel (600, 600)
        surface.blit(self.img, self.coord)

