import pygame


class Button():
    def __init__(self, x, y, image_location, scale):

        image_raw = pygame.image.load(image_location).convert_alpha()

        self.image = pygame.transform.scale(image_raw, #Image to transform
                                            (int(image_raw.get_width() * scale), #Widht transform
                                             int(image_raw.get_height() * scale))) #Height transform
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.clicked = False #Is the button pressed

    def draw(self, surface):
        
        action = False #If an action should be made when the button is clicked

        #get mouse position
        pos = pygame.mouse.get_pos()

        #check if mouse is over the button and is clicked
        if self.rect.collidepoint(pos):
            if (pygame.mouse.get_pressed()[0] == 1 #Left click is clicked
                and self.clicked == False): 

                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0: #Not clicked
            self.clicked = False


        #Draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action