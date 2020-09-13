import pygame
 
class Ship():

    def __init__(self, gs, screen):

        self.screen = screen
        self.gs = gs

        # Loading ship image
        self.image = pygame.image.load('shipim.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # start ship at bottom center
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # ship center
        self.center = float(self.rect.centerx)

        # ship movement flags
        self.moveright = False
        self.moveleft = False
        self.moveup = False
    
    def center_ship(self):
        self.center = self.screen_rect.centerx

    def update(self):
        if self.moveright and self.rect.right < self.screen_rect.right:
            self.center += self.gs.ship_speed
        elif self.moveleft and self.rect.left > 0:
            self.center -= self.gs.ship_speed
        elif self.moveup:
            self.rect.centery = self.rect.centery - 1
        else:
            pass

        self.rect.centerx = self.center

    def blitme(self):
        # draws the ship at its current location
        self.screen.blit(self.image, self.rect)

# rect objects:
# work with center, centerx, centery, top, bottom, left, and right elements