import sys 
import pygame

def check_events():
    """Respond to keyboard and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings, screen, unicorn_dude):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    unicorn_dude.blitme()

    # Make the most recently drawn screen visible.
    pygame.display.flip()