################

#track statistics for Alien Invasion
class GameStats():
    #initialize sttistics
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        #Start Alien Invasion in an inactive state
        self.game_active = False
    #initialize statistics that can change during the game
    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
