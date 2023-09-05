import pygame, math 


class Shell:
    def __init__(self, parent, shell_type, weight, muzzle_velocity, fuse_time, x, y):
        self.parent = parent
        self.shell_type = shell_type
        self.weight = weight # in kilograms(kg)
        self.muzzle_velocity = muzzle_velocity # in meters per second(m/s)
        self.fuse_time = fuse_time
        self.x = x
        self.y = y
        
    def move(self):
        self.x += (self.muzzle_velocity * math.cos(self.parent.barrel_elevation))
        self.y += (self.muzzle_velocity * math.sin(self.parent.barrel_elevation))
        
#------------------------------------------------

class Turret:
    def __init__(self, parent, x_dim, y_dim, x_cord, y_cord, num_barrels, caliber, rate_of_fire, barrel_elevation):
        self.parent = parent
        self.x_dim = x_dim
        self.y_dim = y_dim
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.num_barrels = num_barrels
        self.caliber = caliber # Caliber will be in millimeters(mm)
        self.rate_of_fire = rate_of_fire
        self.barrel_elevation = barrel_elevation
        self.loaded = False # Game will start with turrets empty
        
        
    def draw(self, surface):
        turret_color = (255, 0, 0)  # Red color for the turret
        barrel_color = (0, 0, 255)  # Blue color for the barrels

        # Draw the turret
        turret_rect = pygame.Rect(self.x_cord, self.y_cord, self.x_dim, self.y_dim)
        pygame.draw.rect(surface, turret_color, turret_rect)

        # Calculate barrel positions based on num_barrels
        if self.num_barrels == 1:
            barrel_rect = pygame.Rect(self.x_cord + self.x_dim // 2 - self.caliber // 2, self.y_cord + self.y_dim // 2 - self.barrel_elevation - 10 // 2, self.caliber, 10)
            pygame.draw.rect(surface, barrel_color, barrel_rect)
        elif self.num_barrels == 2:
            barrel_spacing = 2
            barrel_rect_left = pygame.Rect(self.x_cord + self.x_dim // 2 - self.caliber // 2 - barrel_spacing - self.caliber, self.y_cord + self.y_dim // 2 - self.barrel_elevation - 10 // 2, self.caliber, 10)
            barrel_rect_right = pygame.Rect(self.x_cord + self.x_dim // 2 + barrel_spacing, self.y_cord + self.y_dim // 2 - self.barrel_elevation - 10 // 2, self.caliber, 10)
            pygame.draw.rect(surface, barrel_color, barrel_rect_left)
            pygame.draw.rect(surface, barrel_color, barrel_rect_right)
        
    
    def fire(self):
        if self.loaded == True:
            self.shell.move() # x,y coordinates
            self.loaded = False
        
        
        

        
        
        