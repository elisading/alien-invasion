import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self,gs,screen,ship):
        super().__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, gs.bullet_width, gs.bullet_height) # initialize bullet at 0,0
        # correct position
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)

        self.color = gs.bullet_color
        self.speed_factor = gs.bullet_speed


    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)


