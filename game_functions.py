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
    """Respond to keyreleases."""
    if event.key == pygame.K_RIGHT:
        unicorn_dude.moving_right = False
        check_sprite_movement(unicorn_dude, 'right')
    elif event.key == pygame.K_LEFT:
        unicorn_dude.moving_left = False
        check_sprite_movement(unicorn_dude, 'left')
    elif event.key == pygame.K_UP:
        unicorn_dude.moving_up = False
        check_sprite_movement(unicorn_dude, 'up')
    elif event.key == pygame.K_DOWN:
        unicorn_dude.moving_down = False
        check_sprite_movement(unicorn_dude, 'down')

def check_sprite_movement(unicorn_dude, direction):
    """Check to see if Unicorn Dude is currently moving"""
    if unicorn_dude.moving_up or unicorn_dude.moving_down or unicorn_dude.moving_left or unicorn_dude.moving_right:
        unicorn_dude.is_moving = True
    else:
        unicorn_dude.is_moving = False
        unicorn_dude.set_standing_image(direction)

def update_screen(ai_settings, screen, unicorn_dude):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    unicorn_dude.blitme()

    # Make the most recently drawn screen visible.
    pygame.display.flip()