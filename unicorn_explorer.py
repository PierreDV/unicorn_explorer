import pygame

from settings import Settings
from unicorn_dude import UnicornDude
import game_functions as gf

def run_game():
    # Initialize pygame, settings and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Unicorn Explorer")

    # Make a unicorn dude.
    unicorn_dude = UnicornDude(ai_settings, screen)

    # Start the main loop for the game.
    while True:
        gf.check_events(unicorn_dude)
        unicorn_dude.update()
        gf.update_screen(ai_settings, screen, unicorn_dude)

run_game()