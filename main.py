#.................................................................................
#                                       FINAL PROJECT
#                                      Space Invaders!
# Weekly Log
#     Week 1: Decided I was going to try and make a realistic 8-ball pool game that used physics to make the ball roll
#             and slow down as they do in real life.  I started by trying to find a good template to base my game off of.
#     Week 2: This week I had found a 60 or 70 line code that displayed a pool table and had a ball move around the screen
#             until it entered a pocket.  After having this I was trying to add to the code, but didn;t quite understand
#             how to go a bout it.  I then looked at more games on Github and found a few games.  After spending a few
#             days trying to figure out how they worked I decided to change my project.  I didn't want to just copy and
#             paste code so I started on the aline project in Python Crash Course so I could build a foundation of
#             understanding how pygame works.  At the end of the week I set up the foundational code and the settings.
#     Week 3: This week I started by adding the image of teh ship to the screen.  I then started to add the code to make
#             the ship move left and right along with setting up a way for the speed of the ship to change and boundaries
#             for where the ship can move.
#     Week 4: Day 1: Try and finish adding commnets to my existing code do I don't get confused and know what is going
#                    on when I try and personalize the game.  After I am going to try and get github working
#             Day 2: Finish setting up Github and then continue with the game tutorial from Python Crach Course
#             Day 3: Continue with the crash course game
#     Week 5: Day 1: Present current project and start adding aliens with time I have left.
#             Day 2: Finish the presentations and continue setting up the enemies and making them move down the screen
#             Day 3: Continue to add the enimies and enable the bullets to kill them
#     Week 6: Day 1: Gone for confirmation class
#             Day 2: Add a play button and spped up the game when a fleet is destoryed
#             Day 3: Begin adding a scoring system to give points and tell how many ships are left
#             Day 4: Fix the scoring system so that all ships that are hit give points and start adding a high score
#                    tracker, an image that tells you what level you are on and let the player know how many ships are
#                    left until they die.  Finish this over the weekend.
# Sources
#     Python Crash Course Project 1

#import libraries
import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf

#main game function
def run_game():
    # Initialize game and create screen objects.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #make the play button
    play_button = Button(ai_settings, screen, "Play")
    #create an instance to store game statistics and make a scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    #make groups to store the ship, bullets and aliens in
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    #creating the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)
    #Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
#runs the game
run_game()