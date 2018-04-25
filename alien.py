##############

#libraries
import pygame
from pygame.sprite import Sprite

#create an alien class
class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        #initialize the alien and set its starting position
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        #load the alien image and set its rect attribute
        self.image = pygame.image.load('enemy1.png')
        self.rect = self.image.get_rect()
        #start each new alien neat the top left screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        #store the alien's exact position
        self.x = float(self.rect.x)
    #draw the current location of the alen
    def blitme(self):
        self.screen.blit(self.image, self.rect)
    #move the alien left or right
    def update(self):
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x
    #return true is the alien is at the edge of the screen
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True