import sys
import pygame
from Ship import Ship

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Naval Battle Simulator")

WHITE = (255,255,255)

SHIP_WIDTH, SHIP_HEIGHT = 25, 25
color_red = (255,0,0)

ship1 = Ship(0,200,SHIP_WIDTH,SHIP_HEIGHT,color_red)
ship_velocity = 5

FPS = 30
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # User clicked the close button, exit the game
            pygame.quit()
            sys.exit()

    screen.fill(WHITE)
    
    ship1.draw(screen)
    
    if ship1.x < WINDOW_WIDTH - 30:
        ship1.x += ship_velocity 

    # Update the display
    pygame.display.update()
    
    clock.tick(FPS)


