################

#import libraries
import pygame

#set up a class for the ship that has functions for how to move, shoot, etc.
class Ship():
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings
        #Load the ship image and get its rect(rectangular position coordinates)
        self.image = pygame.image.load('main_ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        #store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)
        #Movement flags
        self.moving_right = False
        self.moving_left = False
    #function to check if a key is pressed and move the ship accordingly
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center
    def blitme(self):
        #draw the ship at its current location
        self.screen.blit(self.image, self.rect)