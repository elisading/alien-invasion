import pygame 
from pygame.sprite import Sprite 

class Alien(Sprite):

    def __init__(self, gs, screen):
        super().__init__()
        self.screen = screen
        self.gs = gs

        self.image = pygame.image.load('alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width 
        self.rect.y = self.rect.height 
        self.x = float(self.rect.x)

    def check_edges(self): # check if alien is at the screen edge
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def blitme(self): # draws an alien
        self.screen.blit(self.image,self.rect)

    def update(self):
        self.x += (self.gs.alien_speed*self.gs.direction)
        self.rect.x = self.x

 #   horizontalspace = gs.screen_width - (2*self.rect.x)
 #   numberaliens_x = horizontalspace/(2*self.rect.x)