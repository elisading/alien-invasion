import sys
import pygame
from bullet import Bullet 
from aliens import Alien 
from time import sleep

def check_events(gs, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # exits game if window is closed
            sys.exit()
        elif event.type == pygame.KEYDOWN: # commands for keypresses (Left and Right)
            check_keydowns(event, gs, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyups(event,ship)        

def check_keydowns(event, gs, screen, ship, bullets): # instruction for keydowns
    if event.key == pygame.K_RIGHT: 
        ship.moveright = True
    elif event.key == pygame.K_LEFT:
        ship.moveleft = True
    elif event.key == pygame.K_SPACE:
        if len(bullets) < gs.bullets_allowed: # limits number of bullets
            new_bullet = Bullet(gs, screen, ship)
            bullets.add(new_bullet)
    elif event.key == pygame.K_UP:
        ship.moveup = True
    elif event.key == pygame.K_q:
        sys.exit()
    else:
        pass

def check_keyups(event, ship): # instruction for keyups
    if event.key == pygame.K_RIGHT:
        ship.moveright = False
    elif event.key == pygame.K_LEFT:
        ship.moveleft = False
    elif event.key == pygame.K_UP:
        ship.moveup = False
    else:
        pass

def get_num_x(gs, alien_w): # calculate how many aliens to put on the screen horizontally
    horizontalspace = gs.screen_width - (2*alien_w)
    numberaliens_x = int(horizontalspace/(2*alien_w))
    return numberaliens_x 

def get_num_rows(gs,ship_height,alien_height):
    yspace = (gs.screen_height - (3*alien_height) - ship_height)
    num_rows = int(yspace/(2*alien_height))
    return num_rows

def create_alien(gs, screen, aliens, alien_num, row_number): # creates 1 alien and adds to row
    alien = Alien(gs, screen)
    alien_w = alien.rect.width
    alien.x = alien_w + (2*alien_w)*alien_num
    alien.rect.x = alien.x 
    alien.rect.y = alien.rect.height + (2*alien.rect.height*row_number)
    aliens.add(alien)

def create_fleet(gs, screen, ship, aliens):
    alien = Alien(gs, screen)
    numberaliens_x = get_num_x(gs, alien.rect.width)
    number_rows = get_num_rows(gs, ship.rect.height, alien.rect.height)
    for row_num in range(number_rows):
        for alien_num in range(numberaliens_x):
            create_alien(gs, screen, aliens, alien_num, row_num)

def fleet_edges(gs, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_dir(gs,aliens)
            break

def change_fleet_dir(gs, aliens):
    for alien in aliens.sprites():
        alien.rect.y += gs.drop_speed
    gs.direction *= -1

def update_aliens(gs, stats, screen, ship, aliens, bullets):
    fleet_edges(gs,aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship,aliens): # 2 arguments, checks for collisions between sprite (ship) and group (aliens)
        print("Ship Hit!")
        ship_hit(gs, stats, screen, ship, aliens, bullets)

def update_bullets(gs, screen, ship, aliens, bullets):
    bullets.update() # reminder, too many groups slow the game, check while loop
    for bullet in bullets.copy(): # get rid of old bullets
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet) 
    check_BAcollisions(gs, screen, ship, aliens, bullets)

def check_BAcollisions(gs, screen, ship, aliens, bullets): # checks for collisions between bullets and aliens
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True) # False, True for bullets that stay active after collision
    if len(aliens) == 0:
        bullets.empty()
        create_fleet(gs,screen,ship,aliens)

def check_aliens_bottom(gs, stats, screen, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(gs, stats, screen, ship, aliens, bullets)
            break

def update_screen(gs,screen,ship,aliens,bullets):
    screen.fill(gs.background_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    pygame.display.flip() # makes the screen visible

def ship_hit(gs, stats, screen, ship, aliens, bullets): # reset the game if ship is hit, subtract 1 from limit
    stats.ships_left -= 1
    aliens.empty() # empty groups
    bullets.empty()

    create_fleet(gs,screen,ship,aliens)
    ship.center_ship

    sleep(0.5) # pause game

