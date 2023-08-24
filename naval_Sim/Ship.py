import pygame

class Ship:
    def __init__(self,x,y,height,width,color):
        self.x = x # Initial starting position x-cord
        self.y = y # Initial starting position y-cord
        self.height = height
        self.width = width
        self.color = color
        
    def draw(self,screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        
    def move(self,x,y):
        self.x += x
        self.y += y
            

        
        