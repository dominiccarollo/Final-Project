############

#create the class settings to set up the main specs for the screen and settings of the assets
class Settings():
    def __init__(self):
        #initialize the game's static settings
        #settings for the screen
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (195, 255, 234)
        #ship settings
        self.ship_limit = 2
        #settings for the bullets
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        #settings for the aliens
        self.fleet_drop_speed = 10
        #how quickly the game speeds up
        self.speedup_scale = 1.2
        self.initialize_dynamic_settings()
    #initialize the settings that change throughout the game
    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 2 # the number is one less than the number of ships you want
        self.alien_speed_factor = 1
        self.fleet_direction = 1 #(if fleet_drection is 1 go right, if -1 go left)
        #scoring
        self.alien_points = 50
    #increase the speed settings
    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
