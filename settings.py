############

#create the class settings to set up the main specs for the screen and settings of the assets
class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (195, 255, 234)
        #ship settings
        self.ship_speed_factor = 1.5
        #settings for the bullets
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60