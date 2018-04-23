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
#             Day 3: Continue with the crash course game pg 264

#import libraries
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

#main game function
def run_game():
    # Initialize game and create screen objects.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings, screen)
    #make a group to store bullets in
    bullets = Group()
    #Set the background color.
    bg_color = (195, 255, 234)
    # Start the main loop for the game.
    while True: 
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)
#runs the game
run_game()