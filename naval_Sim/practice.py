import sys
import pygame
from Ship import Ship
from turrets import Turret, Shell

#-------------------

def moveFourCorners(ship: Ship): 
    # Problem here, you reassign flags to False everytime, so it will only move once
    topLeft = False
    topRight = False
    bottomLeft = False
    bottomRight = False
    
    # 600H, 800W
    if ship.x == 0 and (ship.y == 0 or ship.y < 775):
        topLeft = True
        topRight = False
        bottomLeft = False
        bottomRight = False
    elif ship.y == 775 and (ship.x == 0 or ship.x < 775):
        topLeft = False
        topRight = False
        bottomLeft = True
        bottomRight = False
    elif ship.x == 775 and (ship.y == 775 or ship.y > 0):
        topLeft = False
        topRight = False
        bottomLeft = False
        bottomRight = True
    elif ship.y == 0 and (ship.x == 775 or ship.x > 0):
        topLeft = False
        topRight = True
        bottomLeft = False
        bottomRight = False
        
    if topLeft:
        ship.move(0,5)
    elif bottomLeft:
        ship.move(5,0)
    elif bottomRight:
        ship.move(0,-5)
    elif topRight:
        ship.move(-5,0)

#-------------------

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 800, 800

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Naval Battle Simulator")

WHITE = (255,255,255)

SHIP_WIDTH, SHIP_HEIGHT = 25, 25
color_red = (255,0,0)

ship1 = Ship(0,0,SHIP_WIDTH,SHIP_HEIGHT,color_red)
turret1 = Turret(ship1,10,10,400,400,2,50,10,0)

FPS = 30
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # User clicked the close button, exit the game
            pygame.quit()
            sys.exit()

    screen.fill(WHITE)
    
    turret1.draw(screen)
    
    # Update the display
    pygame.display.update()
    
    clock.tick(FPS)
    
    
    


