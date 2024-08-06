import pygame

from UI.background.bouncingBackground import BouncingBackground

screen_dimension = 600


pygame.init()
screen = pygame.display.set_mode((screen_dimension,screen_dimension))
pygame.mouse.set_visible(0)
pygame.display.set_caption('Tic Tac Toe')


#The game start with the main background
main_backGround = BouncingBackground("./rsc/background/main_background.png", 200, screen_dimension)



running = True
while running:
    
    x, y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    main_backGround.UpdateCoords()
    main_backGround.show(screen)
    pygame.display.update()




#from Game.game import game
#
#
#print("Hello world")
#
#currentGame = game()
#currentGame.playGame()