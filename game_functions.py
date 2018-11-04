import sys 
import pygame

def check_events(unicorn_dude):
    """Respond to keyboard and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, unicorn_dude)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, unicorn_dude)
            
def check_keydown_events(event, unicorn_dude):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        unicorn_dude.moving_right = True
    elif event.key == pygame.K_LEFT:
        unicorn_dude.moving_left = True
    elif event.key == pygame.K_UP:
        unicorn_dude.moving_up = True
    elif event.key == pygame.K_DOWN:
        unicorn_dude.moving_down = True

def check_keyup_events(event, unicorn_dude):
    """Respond to keyreleases"""
    if event.key == pygame.K_RIGHT:
        unicorn_dude.moving_right = False
    elif event.key == pygame.K_LEFT:
        unicorn_dude.moving_left = False
    elif event.key == pygame.K_UP:
        unicorn_dude.moving_up = False
    elif event.key == pygame.K_DOWN:
        unicorn_dude.moving_down = False

def update_screen(ai_settings, screen, unicorn_dude):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    unicorn_dude.blitme()

    # Make the most recently drawn screen visible.
    pygame.display.flip()