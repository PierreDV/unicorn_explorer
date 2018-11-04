import sys 
import pygame

def check_events(unicorn_dude):
    """Respond to keyboard and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # Move unicorn dude to the right.
                unicorn_dude.moving_right = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                unicorn_dude.moving_right = False

def update_screen(ai_settings, screen, unicorn_dude):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    unicorn_dude.blitme()

    # Make the most recently drawn screen visible.
    pygame.display.flip()