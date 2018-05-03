#################

#import libraries
import pygame

#a class for manipulation the scoring stats
class Scoreboard():
    def __init__(self, ai_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        #add font settings for scoring info
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        #prepare the initial score image
        self.prep_score()
    #turn the score into a rendered image
    def prep_score(self):
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)
        #display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    #draw the score on the screen
    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)