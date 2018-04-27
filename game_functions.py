#####################

#import libraries
import sys
from time import sleep
import pygame
from bullet import Bullet
from alien import Alien

#set up functions to change event.key to true or false depending on if a key is pressed or not
def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
#check to see if a key is no longer being pressed
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
#updates the screen when called upon
def update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button):
    #Update images on the screen and flip to the new screen.
    #Redraw the screen during each pass through the loop
    screen.fill(ai_settings.bg_color)
    #redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    #draw play button if screen is inactive
    if not stats.game_active:
        play_button.draw_button()
    #Make the most recently drawn screen visible.
    pygame.display.flip()

##Bullet functions
#fire a bullet if the limit has not been reached
def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
#if a bullet is fired have it move up the screen and delete it when it goes off the screen
def update_bullets(ai_settings, screen, ship, aliens, bullets):
    #update the position of bullets and get rid of old bullets
    bullets.update()
    #Get rid of bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)
#check if a bullet has hit an alien and if so get rid of the alien and bullet
def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    #If fleet is destroyed then delete bullets and add new fleet
    if len(aliens) == 0:
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)

##Alien functions
#determine the number of aliens that can fit in a row
def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x
#deteremine how many rows of aliens can fit
def get_number_rows(ai_settings, ship_height, alien_height):
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows
#create an alien and put it in the row
def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)
#create the fleet of aliens
def create_fleet(ai_settings, screen, ship, aliens):
    #create the alien and find the number of aliens in a row
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    #create the first row of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)
#respond to ship being hit by alien
def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    if stats.ships_left > 0:
        stats.ships_left -= 1
        #empty the lis of aliens and bullets
        aliens.empty()
        bullets.empty()
        #create a new fleet and center the ship
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        #pause
        sleep(0.5)
    else:
        stats.game_active = False
#check if any aliens have reached the bottom of the screen
def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            #treat hitting the bottom as hitting the ship
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break
#update the positions of all aliens in the fleet
def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    #look for alien-ship collisions
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
    #look for aliens hitting the bottom of the screen
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)
#respond appropriately if any aleins reaches an edge
def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break
#drop the entire fleet and change the fleet's direction
def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1