#####################

#import libraries
import sys
import pygame
from bullet import Bullet

#set up functions to chnage event.key to true or false depending on if a key is pressed or not
def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key ==pygame.K_SPACE:
        #create a new bullet and add it to the bullets group
        if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)
def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
#check when an event happens such as a key press
def check_events(ai_settings, screen, ship, bullets):
    #respond to keypresses and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
def update_screen(ai_settings, screen, ship, bullets):
    #Update images on the screen and flip to the new screen.
    #Redraw the screen during each pass through the loop
    screen.fill(ai_settings.bg_color)
    #redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    #Make the most recently drawn screen visible.
    pygame.display.flip()
def update_bullets(bullets):
    #update the position of bullets and get rid of old bullets
    #update bulet positions
    bullets.update()
    #Get rid of bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)