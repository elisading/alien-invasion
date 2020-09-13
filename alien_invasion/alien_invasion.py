import sys
import pygame
from pygame.sprite import Group 
from settings import Settings
from ship import Ship
#from aliens import Alien 
from game_statistics import GameStats
import game_functions as gf

def run_game():
    pygame.init() # Initialize game and screen object
    gs = Settings() # initialize from Settings class
    # gs stands for game settings
    screen = pygame.display.set_mode((gs.screen_width,gs.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(gs,screen)
    bullets = Group()
    aliens = Group()
    stats = GameStats(gs)
#   alien = Alien(gs, screen)
    gf.create_fleet(gs,screen,ship,aliens)

    while True:

        gf.check_events(gs, screen, ship, bullets)
        ship.update()
        gf.update_bullets(gs, screen, ship, aliens, bullets)
        gf.update_aliens(gs, stats, screen, ship, aliens, bullets)
        gf.update_screen(gs, screen, ship, aliens, bullets)

run_game()

